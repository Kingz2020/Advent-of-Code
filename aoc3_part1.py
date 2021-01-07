import pandas as pd

df = pd.read_csv('data/map.csv', header=None)


def next_sign(df=df, index=0, col_position=1, col=3, row=1):
    """gets a dataframe and returns what is at x columns and y rows """
    idx = index + row
    col = (col_position+col) % 31
    sign = df[0][index+row][(col_position+col) % 31]
    return idx, col, sign


def get_all_states(df, start_col, start_row):
    """Gets all the trees(#) found under the condition 
    until the end of the dataframe file an returns the value"""
    idx = start_row
    col = start_col
    counter = 0
    while idx < len(df)-1:
        idx, col, sign = next_sign(df, idx, col, 3, 1)
        # print(idx,col,sign)
        if sign == '#':
            counter += 1
    return print(f'the no. of trees is {counter}')


get_all_states(df, 0, 0)
