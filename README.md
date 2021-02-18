# Object detection using UnrealCV

 UnrealCV 가상 시뮬레이션 환경에서 **detectron2**를 이용한 object detection을 진행한다.

 [detectron2](https://github.com/facebookresearch/detectron2)는 Facebook AI Research에서 제공하는 객체 감지 알고리즘으로, pytorch deep learning framework에 의해 구동된다. 
  

### 환경 (요구 사항)
* Ubuntu 16.04
* python 3.8 (3.6 이상)
* GTX 1060
* PyTorch 1.7.1 (1.5 이상)
* CUDA 10.1
* OpenCV 4.5.1
  
  
  
## 1. Repository cloning
```
git clone https://github.com/boookk/Use_UnrealCV.git
```



## 2. Create virtual environment
```
cd Use_UnrealCV
conda env create -f environment.yml
```



## 3. Installing UnrealCV

 다양한 시뮬레이션 환경 중 '[UnrealCV](https://unrealcv.org/)'를 사용하였다.

 UnrealCV는 Unreal Engine 4 (UE4)를 사용한 시뮬레이션으로 [Model Zoo](http://docs.unrealcv.org/en/master/reference/model_zoo.html#rr)에서 컴파일된 게임 바이너리를 제공한다. 

 Model Zoo에서 제공하는 게임 바이너리를 다운 받는다. (Ex. RealisticRendering)
  
```
sh virtual_env.sh
```
위의 명령어를 입력하거나, Model Zoo 링크를 통해 게임 바이너리를 다운 받을 수 있다.



## 4. Run

#### Object detection
 * Instance Segmentation (+ bbox, accuracy)
 ```
 python code/instance_Seg.py
 ```
 * Semantic Segmentation
 ```
 python code/semantic_Seg.py
 ```
