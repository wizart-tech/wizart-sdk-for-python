# Wizart Vision SDK for Python


The Wizart Vision SDK is a set of software development tools and libraries provided by Wizart.ai that enables developers to integrate the Wizart Vision API's capabilities into their applications more easily. The SDK acts as a bridge between the Vision API and the developer's application by providing a standardized set of functions and interfaces that the developer can use to access the API's functionality.

Looking for more documentation?

* [Wizart Vision API Review](https://wizart.ai/vision-api)
* [Wizart Vision SDK for JavaScript](https://github.com/wizart-tech/wizart-sdk-for-js)

⭐️ Start using Wizart Vision API with the [RapirAPI platform](https://rapidapi.com/wizart-ai-wizart-ai-default/api/vision-api).

## Features

Wizart Vision technology base consists of several core components that power our computer vision solutions. These include segmentation, detection, reconstruction, and analysis, each of which plays a critical role in enabling advanced visual capabilities. Below are links to learn more about each component and how they contribute to our powerful Vision API.

- [Technologies for Home Interior](https://wizart.ai/technologies)
- [Indoor Semantic Segmentation](https://wizart.ai/segmentation)
- [Indoor Object Detection](https://wizart.ai/detection)
- [3D Interior Layout Reconstruction](https://wizart.ai/reconstruction)
- [Indoor Scene Analysis & Classification](https://wizart.ai/analysis)

https://user-images.githubusercontent.com/408283/221159389-16f146f9-fda7-4dfb-84e4-16d2d1500e59.mp4

## Installation
```shell
pip3 install wizart-vision
```
## Authentication
Once you received X-RapidAPI-Key, you need initialize vision client
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
- feature - entity or surface name, available in Wizart Vision SDK

```python
from wizart.vision import ComputerVisionClient as vc

# use this feature object for segmentation, detection, reconstruction and interior calls
vc.feature

# currently supported feature entities
vc.feature.WALL
vc.feature.CEILING
vc.feature.FLOOR
vc.feature.WINDOW

# use this object for different analysis calls
vc.analysis_types

# currently supported analysis types
vc.analysis_types.CAMERA
vc.analysis_types.IMAGE_INFO
vc.analysis_types.INTERIOR_TYPE
```

### Segmentation
Indoor scene semantic decomposition process.

Obtaining indoor segmentation mask
```python
mask = client.segmentation(
    resource="file system path or http link to image"
)
```
Segmentation by feature (i.e. by surface object)
```python
mask = client.segmentation(
    resource="file system path or http link to image",
    feature=vc.feature.CEILING
)
```
To obtain only the mask contours, enable the `vectorized` option by setting it to `True`.
```python
mask = client.segmentation(
    resource="file system path or http link to image",
    feature=vc.feature.CEILING,
    vectorized=True
)
```

### Detection
Localize objects coordinates in the photo.

Detect all supported entities
```python
feature = client.detection(
    resource="path to image"
)
```
Single entity detection, e.g. detect only the walls
```python
feature = client.detection(
    resource="path to image",
    feature=vc.feature.WALL
)
```
### Reconstruction
Obtain information about the 3D dimensions (real sizes) and positions of scene objects in the photo.

Reconstruct all supported entities and scene params 
```python
feature = client.reconstruction(
    resource="path to image"
)
```
Reconstruct a specific entity and scene params 
```python
feature = client.reconstruction(
    resource="path to image",
    feature=vc.feature.FLOOR
)
```
### Analyze
The Analysis API includes a set of different computer vision solutions based on neural networks.


Analyse image, interior and camera
```python
feature = client.analysis(
    resource="path to image"
)
```
Perform a specific type of analysis
```python
feature = client.analysis(
    resource="path to image",
    feature=vc.analysis_types.CAMERA
)
```
### Interior
Provides the ability to get all the data on the requested feature that we were able to extract from the uploaded interior photo.

Describe all entities
```python
feature = client.interior(
    resource="path to image"
)
```
Get data for a specific entity
```python
feature = client.interior(
    resource="path to image",
    feature=vc.feature.CEILING
)
```
To obtain only the mask contours, enable the `vectorized` option by setting it to `True`.
```python
mask = client.interior(
    resource="file system path or http link to image",
    vectorized=True
)
```

Supported analysis types and features are listed in [_client_enums.py](wizart-tech/wizart-sdk-for-python/blob/main/wizart/vision/_client_enums.py) 
