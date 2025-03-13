from  setuptools import setup, find_packages
from typing import List

hypen_dot_e='-e .'

def get_requirements(file_path:str)->[List]:
    requirements=[]
    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('/n','') for req in requirements]

        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)

    return requirements

setup(
    name ='AI-Powered-Interview-App',
    version='1.0',
    author='Arpanchakraborty23',
    author_email='arpanchakaborty500@gmail.com',
    url='https://github.com/arpanchakraborty23/AI-Powered-Interview-App.git',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
)