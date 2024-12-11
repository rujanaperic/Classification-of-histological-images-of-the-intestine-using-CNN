from setuptools import setup, find_packages

setup(
    name="classification_of_histological_images",
    version="0.1",
    packages=find_packages(where="development"),
    package_dir={"": "development"},
)