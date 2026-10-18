from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    """this function will return the list of requirements"""
    result = []
    with open(file_path,'r') as file:
        raw_list = file.readlines()
        result = [requirement.replace("\n","") for requirement in raw_list]

        if "-e ." in result:
            result.remove('-e .')
    return result

setup(
    name="mlproject",
    version="0.0.1",
    author="arvinloc",
    author_email="sulvinskijartiom@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)