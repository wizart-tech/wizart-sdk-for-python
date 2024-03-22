import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
CHANGELOG = (HERE / "CHANGELOG.md").read_text()

setup(
    name="wizart-vision",
    version="1.0.6",
    description="Wizart Computer Vision SDK",
    long_description=README + '\n\n' + CHANGELOG,
    long_description_content_type="text/markdown",
    author="Yauheni Dzirvuk",
    author_email="yauheni.dzirvuk@wizart.ai",
    license="MIT License",
    packages=["wizart.vision"],
    install_requires=[
        'numpy>=1.19.2',
        'Pillow>=8.0.0',
        'requests',
        'validators'
    ],
    zip_safe=False
)
