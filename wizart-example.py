import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

from wizart.vision import ComputerVisionClient as vc

client = vc(
    token="Your Token"
)

# -------- SEMANTIC MASK ----------
# mask = client.segmentation(
#     resource=str(BASE_DIR.joinpath('test1.jpg'))
# )
# cv2.imshow('Segmentation Example', mask)
# cv2.waitKey()

# -------- SINGLE MASK ----------
mask = client.segmentation(
    resource=str(BASE_DIR.joinpath('test1.jpg')),
    feature=vc.feature.CEILING
)
cv2.imshow('Segmentation Example', mask)
cv2.waitKey()

# -------- VECTORIZED MASK ----------
# vectorized = client.segmentation(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.feature.CEILING,
#     vectorized=True
# )
# print(vectorized)

# -------- DETECTION ALL -----------
# detection_all = client.detection(
#     resource=str(BASE_DIR.joinpath('test1.jpg'))
# )
# print(detection_all)

# -------- DETECTION BY FEATURE -----------
# feature = client.detection(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.feature.WALL
# )
# print(feature)

# -------- RECONSTRUCTION ALL -----------
# reconstruction_all = client.reconstruction(
#     resource=str(BASE_DIR.joinpath('test1.jpg'))
# )
# print(reconstruction_all)

# -------- RECONSTRUCTION BY FEATURE -----------
# feature = client.reconstruction(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.feature.CEILING
# )
# print(feature)

# -------- ANALYZE ALL -----------
# data = client.analysis(
#     resource=str(BASE_DIR.joinpath('test1.jpg'))
# )
# print(data)

# -------- ANALYZE CAMERA -----------
# data = client.analysis(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.analysis_types.CAMERA
# )
# print(data)

# -------- ANALYZE IMAGE INFO -----------
# data = client.analysis(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.analysis_types.IMAGE_INFO
# )
# print(data)

# -------- INTERIOR ALL -----------
# data = client.interior(
#     resource=str(BASE_DIR.joinpath('test1.jpg'))
# )
# print(data)

# -------- INTERIOR FEATURE -----------
# data = client.interior(
#     resource=str(BASE_DIR.joinpath('test1.jpg')),
#     feature=vc.feature.CEILING
# )
# print(data)