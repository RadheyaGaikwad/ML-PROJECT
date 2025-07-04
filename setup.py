from setuptools import setup, find_packages       #automatically find packages
from typing import List

def get_requirements(file_path: str) -> List[str]:

    "this function will return a list of requirements from the given file path"

    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='ML Project',
    version='0.1',
    author='Radheya',
    author_email='radhegaiwkad76@gmail.com',
    packages=find_packages(),  # Automatically find packages in the current directory   
    install_requires=get_requirements('requirements.txt'),  # List of dependencies

)
