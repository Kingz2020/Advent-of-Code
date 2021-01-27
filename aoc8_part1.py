import pandas as pd


def find_value_of_acc(df, start):
    """"""
    acc = 0
    idx = start
    counter = 0
    while df['sequence'][idx] == -1:
        if df[0][idx] == 'jmp':
            df['sequence'][idx] = counter
            idx = idx + df[1][idx]
            counter += 1
        elif df[0][idx] == 'acc':
            df['sequence'][idx] = counter
            acc += df[1][idx]
            idx += 1
            counter += 1
        elif df[0][idx] == 'nop':
            df['sequence'][idx] = counter
            idx += 1
            counter += 1
    answer = acc
    return print(f'acc = {answer}')


path = "data/day8.csv"
df = pd.read_csv(path, delim_whitespace=True, header=None)
df['sequence'] = -1
find_value_of_acc(df, 0)
