import pandas as pd


def count_elements(path):
    """ gets the file, converts into a dictionary, 
    counts the number of different elements 
    and returns the dataframe"""
    count = 0
    with open(path, 'r') as f:
        groups = f.read().split('\n\n')
    for idx in range(len(groups)):
        word = groups[idx].split('\n')
        no_of_ele = len(word)
        for i in range(no_of_ele-1):
            word[0] = word[0]+word[i+1]
        count += len(''.join(set(word[0])))
    return count


path = 'data/day6.txt'

nr = count_elements(path)
nr
