import pandas as pd


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


def converter(letter, start_value, end_value):
    """Converts a letter F or B, with the lowest and highest number, to a new lower and higher number."""
    if letter == "F":
        return start_value, (start_value + end_value - 1)/2
    elif letter == "B":
        return (start_value + end_value + 1)/2, end_value


df = pd.read_csv('data/boarding.csv', header=None)
df.columns = ['code']


def find_all_seatid(df):
    """"""
    seatids = []
    for idx, row in df.iterrows():
        seatids.append(find_row(row[0]) * 8 + find_column(row[0]))
    return seatids


seatids = find_all_seatid(df)

for idx in range(int(max(seatids))):
    if idx not in seatids and idx-1 in seatids and idx+1 in seatids:
        my_seat = idx
        break
print(f'(part2 answer is {my_seat}')
