OUTPUT_FILES_DIRECTORY = "./output_files/"

def export(dataframe: list, filename: list, format: str = 'parquet'):
    """ 
        takes dataframes and exports them to /output_files dir
        in provided file format (default: .parquet) 
    """
    func_to_extension = getattr(dataframe, f"to_{format}")
    func_to_extension(OUTPUT_FILES_DIRECTORY + filename + f".{format}", index=False)
