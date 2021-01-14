import pandas as pd

df = pd.read_csv('data/boarding.csv', header=None)


def converter(letter, start_value, end_value):
    """Converts a letter F or B, with the lowest and highest number,
    to a new lower and higher number."""
    if letter == "F":
        return start_value, (start_value + end_value - 1)/2
    elif letter == "B":
        return (start_value + end_value + 1)/2, end_value


def find_row(word):
    """goes through the letters of the string and finds the row."""
    idx = 0
    first = 0
    second = 127
    while idx < 7:
        first, second = converter(word[idx], first, second)
        idx += 1
    return first


def find_column(word):
    """"""
    idx = 7
    first = 0
    second = 7
    while idx < 10:
        if word[idx] == "R":
            first, second = converter('B', first, second)
        elif word[idx] == "L":
            first, second = converter('F', first, second)
        idx += 1
    return second


def find_highest_seatid(df):
    """"""
    highest = 0
    for row in df.iterrows():
        seatid = find_row(row[0]) * 8 + find_column(row[0])
        if seatid > highest:
            highest = seatid
    return highest


high = find_highest_seatid(df)
print(f'the answer is {high}')
