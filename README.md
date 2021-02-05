# Use detectron2 with UnrealCV

 시뮬레이션 환경에서 pytorch 기반의 **detectron2**를 이용한 object detection 진행

### 환경 (요구 사항)
* Ubuntu 16.04
* python 3.8 (3.6 이상)
* GTX 1060
* PyTorch 1.7.1 (1.5 이상)
* CUDA 10.1
* OpenCV 4.5.1
  
  
## 1. Installing UnrealCV

 다양한 시뮬레이션 환경 중 '[UnrealCV](https://unrealcv.org/)'를 사용하였다.

 UnrealCV는 Unreal Engine 4 (UE4)를 사용한 시뮬레이션으로 [Model Zoo](http://docs.unrealcv.org/en/master/reference/model_zoo.html#rr)에서 컴파일된 게임 바이너리를 제공한다. 

 해당 시뮬레이션 튜토리얼대로 원하는 게임 바이너리를 다운 받는다. (RealisticRendering)
  
  
## 2. Installing detectron2

 [detectron2](https://github.com/facebookresearch/detectron2)는 Facebook AI Research에서 제공하는 객체 감지 알고리즘이다.

 [설치 가이드](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md)에 따라 설치한다.

Object detection using unrealcv
