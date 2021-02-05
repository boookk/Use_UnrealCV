import numpy as np
import cv2
import os
from unrealcv import client
import sys
import io
from PIL import Image

from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


def read_png(image):
    '''
    Args :
	res (bytes)

    Return :
	np.ndarray : an image of shape (H, W, C) (in BGR order).
	This is the format used by OpenCV.
    '''
    image = Image.open(io.BytesIO(image))
    return np.asarray(image)


if __name__ == '__main__':
    # load config from file and command-line arguments
    cfg = get_cfg()

    model = os.getenv('MODEL_CONFIG', 'mask_rcnn_R_50_FPN_3x.yaml')
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/" + model))
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")

    predictor = DefaultPredictor(cfg)

    # 게임 바이너리와 연결
    client.connect()

    # 게임 바이너리와 연결 확인
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

            # get metadata
            metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
            # visualise
            v = Visualizer(img, metadata=metadata, scale=1.2)
            v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
            img = np.uint8(v.get_image()[:, :, ::-1])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imshow('RealisticRendering', img)
        except:
            pass

    cv2.destroyAllWindows()
