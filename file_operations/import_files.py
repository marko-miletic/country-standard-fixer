import os
import pandas as pd

from path_structure import INPUT_FILES_DIRECTORY


def get_dataframes_and_file_names() -> list:
    """ 
        takes {.format} files from '/files' folder
        and creates dataframes
        ...
        return -> dataframes from input files
    """
    for file in os.listdir(INPUT_FILES_DIRECTORY):
        full_path = os.path.join(INPUT_FILES_DIRECTORY, file)
        file_extension = os.path.splitext(file)[1]
        func_read_extension = getattr(pd, f'read_{file_extension[1:]}')
        yield func_read_extension(full_path), os.path.splitext(file)[0]
