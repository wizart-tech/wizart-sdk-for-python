import base64
import json
from io import BytesIO
import os

import numpy as np
import requests
import inspect
import validators
from PIL import Image

from ._client_enums import FeatureTypes, AnalysisTypes

DEFAULT_SERVER = "https://vision-api.p.rapidapi.com"
DEFAULT_HOST = "vision-api.p.rapidapi.com"


class ComputerVisionClient:
    feature = FeatureTypes
    analysis_types = AnalysisTypes

    def __init__(self, token, endpoint=DEFAULT_SERVER, host=DEFAULT_HOST):
        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if token is None:
            raise ValueError("Parameter 'token' must not be None.")

        self.endpoint = endpoint
        self.host = host
        self.token = token

    def segmentation(self, resource: str, feature: FeatureTypes = '', vectorized=False):
        response = self._request(resource, feature, {'vectorized': vectorized} if vectorized else {})
        if vectorized:
            return self._vectorized_mask_response(response)
        else:
            return self._mask_response(response)

    def detection(self, resource: str, feature: FeatureTypes = ''):
        response = self._request(resource, feature)
        return json.loads(response.content)

    def reconstruction(self, resource: str, feature: FeatureTypes = ''):
        response = self._request(resource, feature)
        return json.loads(response.content)

    def analysis(self, resource: str, feature: AnalysisTypes = ''):
        response = self._request(resource, feature)
        return json.loads(response.content)

    def interior(self, resource: str, feature: FeatureTypes = '', vectorized=False):
        response = self._request(resource, feature, {'vectorized': vectorized} if vectorized else {})
        response_data = json.loads(response.content)
        if not vectorized:
            mask_bytes = base64.b64decode(str(response_data['segmentation']['mask']))
            im = Image.open(BytesIO(mask_bytes))
            response_data['segmentation']['mask'] = np.array(im)

        return response_data

    def _request(self, resource, feature, data={}):
        files = self.create_payload(resource, feature)
        feature_param = '/' + feature if feature else feature
        request_url = self.endpoint + '/' + inspect.stack()[1][3] + feature_param
        return requests.request("POST", request_url, headers={
            "Accept": "application/json",
            "X-RapidAPI-Key": self.token,
            "X-RapidAPI-Host": self.host
        }, data=data, files=files)

    @staticmethod
    def _mask_response(response):
        mask_base64 = json.loads(response.text)['mask']
        mask_bytes = base64.b64decode(str(mask_base64))
        im = Image.open(BytesIO(mask_bytes))
        return np.array(im)

    @staticmethod
    def _vectorized_mask_response(response):
        data = json.loads(response.content)
        if 'vectorized_masks' in data:
            return data['vectorized_masks']
        else:
            return data['vectorized_mask']

    @staticmethod
    def create_payload(resource: str, feature: FeatureTypes):
        if feature and not FeatureTypes.has_value(feature) and not AnalysisTypes.has_value(feature):
            raise ValueError("Undefined FeatureType to request!")
        if ComputerVisionClient.is_valid_url(resource):
            img_bytes = BytesIO(requests.get(resource).content)
        elif os.path.isfile(resource):
            img_bytes = open(resource, 'rb').read()
        else:
            raise ValueError("Invalid resource parameter, please pass an valid url or path to the file!")

        return [('room_image', ('test.jpg', img_bytes, 'image/jpeg'))]

    @staticmethod
    def is_valid_url(url_str):
        return validators.url(url_str)
