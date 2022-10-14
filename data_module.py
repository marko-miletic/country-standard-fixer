import pandas as pd
import standard_values.standardized_values as standardized_values
import dataframes_correction
from file_operations import import_files
from file_operations import export_files


pd.options.mode.chained_assignment = None  # default='warn'

countries_set = standardized_values.get_countries()
codes_set_alpha3 = standardized_values.get_codes_alpha3()
codes_set_alpha2 = standardized_values.get_codes_alpha2()
country_code_combinations = standardized_values.get_country_code_combinations()

dataframes, filenames = import_files.get_dataframes(), import_files.get_filenames()

dataframes_correction.correction(dataframes, countries_set, codes_set_alpha3, codes_set_alpha2, country_code_combinations)

export_files.export(dataframes, filenames, format="csv")
