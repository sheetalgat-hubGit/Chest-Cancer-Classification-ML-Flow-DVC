import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"
# below is the list of files we are creating .github folder in that workflows, .gitkeep } so when we do ci/cd deplsoyementwe will need . github folder and in that workflow folder and inside that main.yaml 
# first create main.yaml file
# just to upload the folder in git hub we are keeping this .gitkeep file bcz github doesnt upload readme.md 

#this is project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",# init.py is constructor file helps to create this folder as local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


# in above file path there is forward slash(/)its not supported in windows (\ supported) so we imported pathlib above to overcome this error (so it will recognise the path)
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #it will seperate the file directory and file name


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")