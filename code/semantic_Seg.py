import numpy as np
import cv2
import psutil
from unrealcv import client
import sys
import io
from PIL import Image
import subprocess

from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


def play(path):
    return subprocess.Popen(path, shell=True)


def setup_cfg():
    # load config from file and command-line arguments
    cfg = get_cfg()

    model_path = "COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml"
    cfg.merge_from_file(model_zoo.get_config_file(model_path))
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(model_path)
    cfg.freeze()
    return cfg


def read_png(res):
    '''
    Input is bytes.

    Return array
    '''
    img = Image.open(io.BytesIO(res))
    return np.asarray(img)


def stop(pid):
    for child in psutil.Process(pid).children(recursive=True):
        child.kill()


if __name__ == '__main__':
    # Start game binary
    path = './RealisticRendering_RL_3.10/RealisticRendering.sh'
    WINDOWS_NAME = path.split('/')[-1].split('.')[0]
    proc = play(path)

    cfg = setup_cfg()

    predictor = DefaultPredictor(cfg)

    # get metadata
    metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])

    # Connecting to a game binary
    client.connect()

    # check game binary connections
    if not client.isconnected():
        print('UnrealCV server is not running.')
        sys.exit(-1)

    # 키보드 'Q'가 눌릴 때까지 게임 바이너리 화면을 가져와 지속적으로 화면 갱신
    while cv2.waitKey(1) != ord('q'):
        try:
            # 게임 바이너리 화면 가져오기
            res = client.request('vget /camera/0/lit png')

            # bytes to array
            img = read_png(res)

            # Always take BGR image as the input
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            outputs = predictor(img)

            # visualise
            v = Visualizer(img, metadata=metadata, scale=1.2)
            x = outputs["sem_seg"].argmax(dim=0)
            out = v.draw_sem_seg(x.to("cpu"))
            img = np.uint8(out.get_image()[:, :, ::-1])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imshow('RealisticRendering', img)
        except:
            pass

    cv2.destroyAllWindows()
    client.disconnect()
    stop(proc.pid)
