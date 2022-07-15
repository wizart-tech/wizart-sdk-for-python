# Wizart Computer Vision SDK for Python

The Computer Vision service provides developers with access to advanced algorithms for processing images and returning information. Computer Vision algorithms analyze the content of an image in different ways, depending on the visual features you're interested in.

You can use Computer Vision in your application to:
- Indoor semantic segmentation
- Interior 3d reconstruction
- Indoor layout and object detection
- Analytics data such as image quality, interior type, camera parameters

Looking for more documentation?

* [SDK reference documentation](https://vision-api.wizart.ai/)
* [Wizart Vision review](https://wizart.ai/vision-api)

If you need access to Wizart Vision API, you can get [API token](https://wizart.ai/trial?source=vision_api) by sending a request

## Installation
```shell
pip3 install wizart-vision
```
## Authentication
Once you received Vision API token, you need initialize vision client
```python
from wizart.vision import ComputerVisionClient as vc

client = vc(
    token="Your token"
)
```
## Usage
See notebook with examples.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wizart-tech/wizart-sdk-for-python/blob/main/wizart-example.ipynb)
The client allows you to perform requests similar to those described in the documentation.
* [segmentation](https://vision-api.wizart.ai/#815786b5-c8a5-42fa-94d5-f7a546e7804b)
* [detection](https://vision-api.wizart.ai/#c07fcc19-4b45-4803-b9cf-e1ab85100ed6)
* [reconstruction](https://vision-api.wizart.ai/#7d66e46a-e70f-4806-9a4d-a63659bf4ad3)
* [analysis](https://vision-api.wizart.ai/#29213748-6fe3-4086-ac90-ae8fe8b1bb7f)
* [interior](https://vision-api.wizart.ai/#c2d17dae-e9cc-4c3f-8097-5201524e015a)

You will operate just with few parameters.

- resource - file system path or http link to the image
- feature - some entity available in Wizart Vision SDK

```python
from wizart.vision import ComputerVisionClient as vc

# use it for segmentation, detection, reconstruction and interior calls
vc.feature

# contains next entities
vc.feature.WALL
vc.feature.CEILING
vc.feature.FLOOR
vc.feature.WINDOW

# use it for analysis call
vc.analysis_types

# contains next entities
vc.analysis_types.CAMERA
vc.analysis_types.IMAGE_INFO
vc.analysis_types.INTERIOR_TYPE
```

### Segmentation
Semantic segmentation
```python
mask = client.segmentation(
    resource="file system path or http link to image"
)
```
Segmentation by feature
```python
mask = client.segmentation(
    resource="file system path or http link to image",
    feature=vc.feature.CEILING
)
```
To get mask contours
```python
mask = client.segmentation(
    resource="file system path or http link to image",
    feature=vc.feature.CEILING,
    vectorized=True
)
```

### Detection
All entities detection
```python
feature = client.detection(
    resource="path to image"
)
```
Single entity detection
```python
feature = client.detection(
    resource="path to image",
    feature=vc.feature.WALL
)
```
### Reconstruction
Multiple 
```python
feature = client.reconstruction(
    resource="path to image"
)
```
Single 
```python
feature = client.reconstruction(
    resource="path to image",
    feature=vc.feature.FLOOR
)
```
### Analyze
Multiple 
```python
feature = client.analysis(
    resource="path to image"
)
```
Single 
```python
feature = client.analysis(
    resource="path to image",
    feature=vc.analysis_types.CAMERA
)
```
### Interior
All
```python
feature = client.interior(
    resource="path to image"
)
```
Single 
```python
feature = client.interior(
    resource="path to image",
    feature=vc.feature.CEILING
)
```