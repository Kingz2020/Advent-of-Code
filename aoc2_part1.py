
import pandas as pd


def count_of_value_in_df(selector, df_position):
    """Goes through all the elements of the df_position and returns the number of selectors"""
    count = 0
    for i in range(len(df_position)):
        if selector == df_position[i]:
            count += 1
    return count


def find_least(df_position):
    """finds the first value before the '-' and returns this value."""
    pos = df_position.find('-')
    return df_position[:pos]


def find_limit(df_position):
    """finds the first value before the '-' and returns this value."""
    pos = df_position.find('-')
    return df_position[pos+1:len(df_position)]


path = 'data/day2_password_data.csv'


def find_nr_valid_passwords(path):
    """function that counts the number of invalid passwords from a list."""

    df2 = pd.read_csv(path, delimiter=" ")
    invalid_password = 0
    valid_password = 0
    for index, rows in df2.iterrows():
        # print(index)
        amount = int(count_of_value_in_df(
            df2['must_have'][index][:1], df2['password'][index]))
        least = int(find_least(df2['range'][index]))
        most = int(find_limit(df2['range'][index]))
        if amount >= least and amount <= most:
            valid_password += 1
            print(index)
        else:
            invalid_password += 1
    return print(f'the number of valid passwords are {valid_password}')


find_nr_valid_passwords(path)
