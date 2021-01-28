import pandas as pd


def changes_state(df, idx):
    """changes the jmp to nop, or nop to jmp"""
    if df[0][idx] == 'jmp':
        df[0][idx] = 'nop'
    elif df[0][idx] == 'nop':
        df[0][idx] = 'jmp'


def find_value_of_acc(df, start):
    """goes through the result of part1, and changes states as required
    when the end of the index is reached it returns the value of acc"""
    acc = 0
    idx = start
    counter = 0
    try:
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
        return acc
    except KeyError:  # out of range
        print(acc)
        return acc


path = "data/day8.csv"
df = pd.read_csv(path, delim_whitespace=True, header=None)
df['sequence'] = -1
answer = find_value_of_acc(df, 0)
print(answer)  # 631
