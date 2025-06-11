from setuptools import find_packages,setup #makes packages of wherever it sees folders or packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]: #created a function where you give file path and return type is string
    '''
    this function will return the list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Vrunda',
    author_email='vrundabrahmbhatt22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   #reads requirement.txt

)
