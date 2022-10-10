OUTPUT_FILES_DIRECTORY = "./output_files/"

def export(dataframes: list, filenames: list, format: str = 'parquet'):
    """ 
        takes dataframes and exports them to /output_files dir
        in provided file format (default: .parquet) 
    """
    for i in range(len(dataframes)):
        print(dataframes[i])
        func_to_extension = getattr(dataframes[i], f"to_{format}")
        func_to_extension(OUTPUT_FILES_DIRECTORY + filenames[i] + f".{format}", index=False)
