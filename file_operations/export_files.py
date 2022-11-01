import os

from path_structure import OUTPUT_FILES_DIRECTORY


def export(dataframe: list, filename: str, extension_type: str = 'parquet'):
    """ 
        takes dataframes and exports them to /output_files dir
        in provided file format (default: .parquet) 
    """
    func_to_extension = getattr(dataframe, f"to_{extension_type}")
    func_to_extension(os.path.join(OUTPUT_FILES_DIRECTORY, f'{filename}.{extension_type}'), index=False)
