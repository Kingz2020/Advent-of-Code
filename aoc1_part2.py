"""Advent of Code day 1 part 2."""

import pandas as pd

path = 'aoc1.xlsx'

df = pd.read_excel(path)


def find_the_3_digits_and_multiply(df):
    """Function to find three digits from a list aoc1.xlsx adding up to 2020.
    returning the value obtained by multiplying the three digits"""
    finished = False
    first_digit = 0
    second_digit = 0
    third_digit = 0
    increment = 0
    second_increment = 0

    while not finished:
        current_second_digit = second_digit + increment
        current_third_digit = third_digit + second_increment
        if df['numbers'][first_digit] + df['numbers'][current_second_digit] + df['numbers'][current_third_digit] == 2020:
            finished = True
            answer = df['numbers'][first_digit] * \
                df['numbers'][current_second_digit] * \
                df['numbers'][current_third_digit]
            print(f"a = {df['numbers'][first_digit]}, b = {df['numbers'][current_second_digit]}, and c = {df['numbers'][current_third_digit]} so the answer is {answer} ")
            break
        elif increment < 199:
            increment += 1
        elif increment == 199:
            if first_digit == 199:
                first_digit = 0
                third_digit += 1
            else:
                first_digit += 1
                increment = 0
        elif first_digit == 199:
            second_increment += 1
            first_digit = 0


find_the_3_digits_and_multiply(df)
