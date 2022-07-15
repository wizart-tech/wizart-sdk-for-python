from enum import Enum


class FeatureTypes(str, Enum):
    WALL = 'walls'
    FLOOR = 'floor'
    CEILING = 'ceiling'
    WINDOW = 'windows'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class AnalysisTypes(str, Enum):
    CAMERA = 'camera'
    IMAGE_INFO = 'image-info'
    INTERIOR_TYPE = 'interior-type'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
