import pandas as pd


def add_contiguous(df, start_index, limit):
    """Adds the contiguous until the limit is reached"""
    sum = 0
    ind = start_index
    while sum < limit:
        sum += df[0][ind]
        ind += 1
    return sum, ind-1


def churn_through_all_rows(df):
    """goes through all rows for result"""
    for index, row in df.iterrows():
        result, last = add_contiguous(df, index, limit)
        if result == limit:
            answer = find_small_and_large(df, index, last)
            print(answer)
            break


def find_small_and_large(df, start_index, last_index):
    """Finds the smallest and largest"""
    smallest = df[0][start_index]
    largest = df[0][start_index]
    for index in range(start_index, last_index+1):
        if df[0][index] > largest:
            largest = df[0][index]
        if df[0][index] < smallest:
            smallest = df[0][index]
    return smallest+largest


limit = 14360655.0  # from part 1
df = pd.read_csv('data/day9.csv', header=None)
churn_through_all_rows(df)
