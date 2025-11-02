from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''This function reads the requirements.txt file and returns a list of dependencies.'''

    requirement_list:List[str] = []

    try:
    #open and read the requirements.txt file
        with open("requirements.txt", "r") as file:
        #read lines from the file
            lines = file.readlines()
        #process each line
        for line in lines:
            #strip whitespace and newline characters
            requirement = line.strip()
            #ignore enpty lines and -e .
            if requirement and requirement != "-e .":
                requirement_list.append(requirement)
    except FileNotFoundError:
       print("requirements.txt file not found. No dependencies will be installed.")

    return requirement_list
print(get_requirements())

setup(
    name = "AI-Travel-Planner",
    version = "0.0.1",
    author  = "asiya irshad",
    author_email = "asiyairshad099@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()

)