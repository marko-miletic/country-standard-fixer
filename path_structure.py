import os


PROJECT_PATH = os.path.split(os.path.abspath(__file__))[0]

# file operations directories
OUTPUT_FILES_DIRECTORY = os.path.join(PROJECT_PATH, 'output_files')
INPUT_FILES_DIRECTORY = os.path.join(PROJECT_PATH, 'files')

STANDARD_VALUES_DIRECTORY = os.path.join(PROJECT_PATH, 'standard_values')
