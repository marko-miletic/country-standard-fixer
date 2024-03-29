import pandas as pd
import numpy as np
from random import randrange
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN = 20
THRESHOLD_FOR_MATCHING_COUNTRY_COLUMN = 12
THRESHOLD_FOR_MATCHING_CODE_COLUMN = 8

MISSING_INSTANCE_VALUES = {np.NaN, None, ''}


pd.options.mode.chained_assignment = None  # default='warn'


def get_country_columns(dataframe: pd.DataFrame, countries_set: set[str]) -> list[str]:
    current_df_columns = dataframe.columns.values.tolist()
    target_columns_countries = []
    for column in current_df_columns:
        """
            from every column in given dataframe takes random 20 entries
            and for each of those check if they are contained in countries_set
            for each entry contained in given sets, counter value increases
            if counter value is bigger than 12 (of 20) then
            given column is considered to be filled with country values
        """
        test_counter_countries = 0
        column_length = len(dataframe[column])
        for _ in range(SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN):
            if dataframe[column][randrange(column_length)] in countries_set:
                test_counter_countries += 1
        if test_counter_countries > THRESHOLD_FOR_MATCHING_COUNTRY_COLUMN:
            target_columns_countries.append(column)
    return target_columns_countries


def get_code_columns_alpha3(dataframe: pd.DataFrame, alpha3_codes_set: set[str]) -> list[str]:
    current_df_columns = dataframe.columns.values.tolist()
    target_columns_codes_alpha3 = []
    for column in current_df_columns:
        """
            from every column in given dataframe takes random 20 entries
            and for each of those check if they are contained in codes_set
            for each entry contained in given sets, counter value increases
            if counter value is bigger than 12 (of 20) then
            given column is considered to be filled with code values
        """
        test_counter_codes = 0
        column_length = len(dataframe[column])
        for _ in range(SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN):
            if dataframe[column][randrange(column_length)] in alpha3_codes_set:
                test_counter_codes += 1
        if test_counter_codes > THRESHOLD_FOR_MATCHING_CODE_COLUMN:
            target_columns_codes_alpha3.append(column)
    return target_columns_codes_alpha3


def get_code_columns_alpha2(dataframe: pd.DataFrame, alpha2_codes_set: set[str]) -> list[str]:
    current_df_columns = dataframe.columns.values.tolist()
    target_columns_codes_alpha2 = []
    for column in current_df_columns:
        """
            from every column in given dataframe takes random 20 entries
            and for each of those check if they are contained in codes_set
            for each entry contained in given sets, counter value increases
            if counter value is bigger than 12 (of 20) then
            given column is considered to be filled with code values
        """
        test_counter_codes = 0
        column_length = len(dataframe[column])
        for _ in range(SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN):
            if dataframe[column][randrange(column_length)] in alpha2_codes_set:
                test_counter_codes += 1
        if test_counter_codes > THRESHOLD_FOR_MATCHING_CODE_COLUMN:
            target_columns_codes_alpha2.append(column)
    return target_columns_codes_alpha2


def correction(
        dataframe: pd.DataFrame,
        countries_set: set[str],
        codes_set_alpha3: set[str],
        codes_set_alpha2: set[str],
        combinations: dict) -> None:
    """
        input -> takes dataframes and standardized data
        maps every column that contains country names or country codes to correct value
    """
    target_columns_countries = get_country_columns(dataframe, countries_set)
    target_columns_codes_alpha3 = get_code_columns_alpha3(dataframe, codes_set_alpha3)
    target_columns_codes_alpha2 = get_code_columns_alpha2(dataframe, codes_set_alpha2)

    for column in target_columns_countries:
        """
            every country value is changed to fit iso3166 standard
            and every code value is changed according to country
        """
        for i in range(len(dataframe[column])):
            if dataframe[column][i] in MISSING_INSTANCE_VALUES:
                """
                    case when value in country column is not defined
                    other columns in that same row are examined for
                    standardized codes that can be used to determine
                    exact country name
                """
                country_value_updated = False
                # bool value that is used to break iterations after country has been found
                for code3_column in target_columns_codes_alpha3:
                    if country_value_updated is True:
                        break
                    if dataframe[code3_column][i] in codes_set_alpha3:
                        for country in combinations:
                            if dataframe[code3_column][i] == combinations[country][0]:
                                dataframe[column][i] = country
                                country_value_updated = True
                                break
                for code2_column in target_columns_codes_alpha2:
                    if country_value_updated is True:
                        break
                    if dataframe[code2_column][i] in codes_set_alpha2:
                        for country in combinations:
                            if dataframe[code2_column][i] == combinations[country][1]:
                                dataframe[column][i] = country
                                country_value_updated = True
                                break

            if dataframe[column][i] not in MISSING_INSTANCE_VALUES:
                if dataframe[column][i] not in countries_set:
                    x = process.extractOne(dataframe[column][i], countries_set, scorer=fuzz.token_set_ratio)
                    dataframe[column][i] = x[0]
                for code_column in target_columns_codes_alpha3:
                    dataframe[code_column][i] = combinations[dataframe[column][i]][0]
                for code_column in target_columns_codes_alpha2:
                    dataframe[code_column][i] = combinations[dataframe[column][i]][1]
