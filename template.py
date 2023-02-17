import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s  ||  %(levelname)s  ||  %(message)s]'
)

while True:
    PROJECT_NAME = input('Enter Project name: ')
    if PROJECT_NAME != "":
        break
logging.info(f'Project created: {PROJECT_NAME}')
        
list_of_files=[
    '.github/workflows/.getkeep',
    '.env',

    'requirements.txt',
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/components/__init__.py',
    f'src/{PROJECT_NAME}/components/data_ingestion.py',
    f'src/{PROJECT_NAME}/components/data_validation.py',
    f'src/{PROJECT_NAME}/components/data_transformation.py',
    f'src/{PROJECT_NAME}/components/model_trainer.py',
    f'src/{PROJECT_NAME}/components/model_evaluation.py',
    f'src/{PROJECT_NAME}/components/model_pusher.py',
    f'src/{PROJECT_NAME}/entity/__init__.py',
    f'src/{PROJECT_NAME}/entity/artifact.py',
    f'src/{PROJECT_NAME}/entity/config.py',
    f'src/{PROJECT_NAME}/logger.py',
    f'src/{PROJECT_NAME}/utils.py',

    'requirements_dev.txt',
    'tests/__init__.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',

    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating new directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f'This file already exists: {filepath}')