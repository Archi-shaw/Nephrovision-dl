import os
from box.exceptions import BoxValueError
import yaml
from .. import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
import base64


# 1. for loading yaml file 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
      Reads  a YAML file and returns its contents as a ConfigureBox object.        
       Args:
       path_to_yaml(Path): The path to the YAML file to be read. path like input  

       Raises: 
        ValueError: if yaml is empty 
        e: empty file

       Returns:
         ConfigBox: A configuebox type
    """
    try: 
       with open(path_to_yaml) as yaml_file:
           content = yaml.safe_load(yaml_file)
           logger.info(f"yaml file: {path_to_yaml} loaded succesfully")
           return ConfigBox(content)
    except BoxValueError:
            raise ValueError("YAML file is empty")
    except Exception as e:
            raise e
    
# 2. making sure all files exist before pipeline runs 

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they don't exist.

    Args:
        path_to_directories (list): List of directory paths to create
        verbose (bool): Whether to log the creation
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")



# 3. Saving a json file 

@ensure_annotations
def save_json(path:Path, data:dict):
    """
      Saves a dictionary to a JSON file 
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


    logger.info(f"json file saved at {path}")

# 4. Loading a json file

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
     """
     Loads a JSON file and returns it contents as a Configue object box(data as class attrribute instead of dict keys)

     """

     with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded from {path}")
        return ConfigBox(content)
        

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data in binary format using joblib

    Args:
        data (Any): the data that needs to be saved
        path (Path): location where file will be saved
    """

    joblib.dump(data, path)
    logger.info(f"Binary file saved at {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
     Loads binary file and returns its content 

     Args: 
       path: path to binary file

      Returns:
      Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str: 
    """
    gets size in KB

    Args:
       path(Path): path to the file 

    Returns :
     Size of the file in KB
    """
    size_in_kb = os.path.getsize(path)/1024
    return f"{size_in_kb:.2f} KB"

@ensure_annotations
def encode_image_to_base64(imgstring,filename):
     imgdata = base64.b64decode(imgstring)
     with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


@ensure_annotations
def decodebase64(imgstring, filename):
    """
    Converts base64 string to image file
    """
    imgdata = base64.b64decode(imgstring)

    with open(filename, "wb") as f:
        f.write(imgdata)