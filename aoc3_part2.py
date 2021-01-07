"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
moves = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
all = []


def get_all_states(df, start_col, start_row, right, down):
    """Gets all the trees(#) found under the condition until the end 
    of the dataframe file an returns the value"""
    idx = start_row
    col = start_col
    counter = 0
    while idx < len(df)-1:
        idx, col, sign = next_sign(df, idx, col, right, down)
        if sign == '#':
            counter += 1
    return counter


def calc_for_all(moves):
    x = 1
    for element in range(len(moves)):
        x = x*get_all_states(df, 0, 0, moves[element][0], moves[element][1])
        all.append(get_all_states(
            df, 0, 0, moves[element][0], moves[element][1]))
    print(x)


calc_for_all(moves)
