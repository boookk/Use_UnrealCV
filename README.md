# Use detectron2

 다양한 입력 데이터에 대해 **detectron2**를 이용한 object detection 진행

 [detectron2](https://github.com/facebookresearch/detectron2)는 Facebook AI Research에서 제공하는 객체 감지 알고리즘이다.

 pytorch deep learning framework에 의해 구동된다. 
  

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
conda env create -f environment.yml
```



## 3. Installing UnrealCV

 시뮬레이션 환경에서 object detection을 수행하지 않을 경우, 이 과정을 생략해도 좋다.
 
 다양한 시뮬레이션 환경 중 '[UnrealCV](https://unrealcv.org/)'를 사용하였다.

 UnrealCV는 Unreal Engine 4 (UE4)를 사용한 시뮬레이션으로 [Model Zoo](http://docs.unrealcv.org/en/master/reference/model_zoo.html#rr)에서 컴파일된 게임 바이너리를 제공한다. 

 Model Zoo에서 제공하는 게임 바이너리를 다운 받는다. (Ex. RealisticRendering)
  


## 4. Run

#### 입력 데이터에 따라

* UnrealCV 
 **게임 바이너리를 실행시킨 상태**에서 코드를 실행해야 한다.

* Image

* WebCam

#### Object detection
 * Panoptic Segmentation (+ bbox, accuracy)


Object detection using unrealcv
