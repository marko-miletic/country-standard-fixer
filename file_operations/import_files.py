import pandas as pd
import os

INPUT_FILES_DIRECTORY = "./files/"

def get_dataframes_and_file_names() -> list:
    """ 
        takes {.format} files from '/files' folder
        and creates dataframes
        ...
        return -> list of created dataframes
    """
    for file in os.listdir(INPUT_FILES_DIRECTORY):
        full_path = os.path.join(INPUT_FILES_DIRECTORY, file)
        file_extension = os.path.splitext(file)[1]
        func_read_extension = getattr(pd, f"read_{file_extension[1:]}")
        yield (func_read_extension(full_path), os.path.splitext(file)[0])