import pandas as pd


def open_file(path):
    """Opens file and returns the list of numbers"""
    with open(path, 'r') as f:
        numbers = f.read().split('\n')
    return numbers


def organise_list(numbers):
    """converts the string to integer and sorts the values in the list.
    Also adds a 0 at the beginnning and highest+3"""
    number = list(map(int, numbers))
    number.append(0)
    number.sort()
    number.append(number[-1]+3)
    return number


def calculate_difference_list(numbers):
    """calculates the difference between the list values"""
    dif_list = []
    for i in range(len(numbers)-1):
        dif_list.append(-(numbers[i]-numbers[i+1]))
    return dif_list


path = 'data/day10.txt'

numbers = open_file(path)
numbers = organise_list(numbers)
dif_list = calculate_difference_list(numbers)
ones = dif_list.count(1)
threes = dif_list.count(3)
print(f'answer = {ones * threes}')
