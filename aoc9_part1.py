
import pandas as pd


def valid_addends(df, start_idx, preamble, search_idx):
    """checks if there are two valid addends in the 25(preamble) preceding rows"""
    for index in range(start_idx, start_idx+preamble):
        if (df[df.loc[start_idx:start_idx+24] == df[0][search_idx]
               - df[0][index]].any()[0]) and (df[0][search_idx] != df[0][index]*2):
            return True  # addends exist
    return False


def search_for_index(df):
    """searches through all rows checking for 'valid addends'"""
    for index1, row in df.iterrows():
        if not valid_addends(df, index1, 25, index1+25):
            print(
                f"the index {index1+25} doesn't have addends, so {df[0][index1+25]}")
            break


path = 'data/day9.csv'
df = pd.read_csv(path, header=None)
search_for_index(df)
