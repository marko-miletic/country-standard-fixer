import pandas as pd
import os

INPUT_FILES_DIRECTORY = "./files/"

def get_dataframes() -> list:
    """ 
        takes {.format} files from '/files' folder
        and creates dataframes
        ...
        return -> list of created dataframes
    """
    dataframes = []
    # TO DO: Replace with magic function :)
    for file in os.listdir(INPUT_FILES_DIRECTORY):
        full_path = os.path.join(INPUT_FILES_DIRECTORY, file)
        file_extension = os.path.splitext(file)[1]
        func_read_extension = getattr(pd, f"read_{file_extension[1:]}")
        dataframes.append(func_read_extension(full_path))
    return dataframes

def get_filenames() -> list:
    """ 
        takes {.format} files from '/files'
        and extract names of those files
        ...
        return -> list of extracted file names
    """
    filenames = []
    # TO DO: Replace with regex matching 
    for file in os.listdir(INPUT_FILES_DIRECTORY):
        filenames.append(os.path.splitext(file)[0])
    return filenames


### tests

def test_get_filenames():
    assert get_filenames() == ["test2", "test1", "test3"]
