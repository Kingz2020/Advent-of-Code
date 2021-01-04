import pandas as pd

path = 'aoc1.xlsx'


def find_the_digits_and_multiply(path):
    df = pd.read_excel('aoc1.xlsx')
    finished = False
    first_digit = 0
    second_digit = 0
    increment = 0
    while finished == False:
        current_digit = second_digit + increment
        if df['numbers'][first_digit] + df['numbers'][current_digit] == 2020:
            finished = True
            first = df['numbers'][first_digit]
            second = df['numbers'][current_digit]
            answer = first * second
            result = print(
                f"a = {first} and b = {second}, so the answer is {answer} ")
            break
        elif increment < 199:
            increment += 1
        elif increment == 199:
            first_digit += 1
            increment = 0
    return result
