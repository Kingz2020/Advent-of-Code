import pandas as pd


def clean_word(start, end, str):
    str = str[start:end]
    str = str.replace(',', '')
    str = str.replace('.', '')
    str = str.replace('bags', '')
    str = str.replace('bag', '')
    str = str.strip()
    return str


def open_file(path):
    """Opens a file and returns the list of groups"""
    with open(path, 'r') as f:
        groups = f.read().split('\n')
    return groups


def get_components(groups):
    """ gets container and a list of bags, ready to be appended to a dictionary"""
    all_dict = {}
    for group in groups:
        container = get_container(group)
        bag = get_bags(group)
        all_dict.update({container: bag})
    return all_dict


def get_bags(sentence):
    """ get the contents of the main bag as a list of strings"""
    bag_names = []
    bag_pos_dict = [(i, nr) for i, nr in enumerate(sentence) if nr.isdigit()]
    for bag_pos in range(len(bag_pos_dict)):
        if bag_pos == len(bag_pos_dict)-1:
            name = clean_word(
                bag_pos_dict[bag_pos][0], len(sentence), sentence)
            bag_names.append(name[2:])
        else:
            name = clean_word(
                bag_pos_dict[bag_pos][0], bag_pos_dict[bag_pos+1][0], sentence)
            bag_names.append(name[2:])
    return bag_names


def get_container(sentence):
    """"""
    pos = sentence.find('contain')
    container = sentence[:pos-6]
    return container


def find_bag(str, dict):
    """counts the amount of keys of a value in a dict"""
    baglist = [key for key, value in dict.items() if str in value]
    return baglist


def count_all(str, dict):
    """
    """
    count = 0
    baglist = find_bag(str, dict)
    new_uniquelist = set()
    count = 0
    new_baglist = baglist
    while len(new_baglist) != 0:
        if count == 0:
            new_baglist = loop_bags(baglist, dict)
            new_uniquelist |= set(new_baglist)
            new_uniquelist |= set(baglist)
            count += 1
        else:
            new_baglist = loop_bags(new_baglist, dict)
            new_uniquelist |= set(new_baglist)
            count += 1
    amount = len(new_uniquelist)
    print(f'all = {new_uniquelist}, answer = {amount}')  # 119


def loop_bags(baglist, dict):
    """loops through bags and returns new list of bags"""
    bags = set()
    for val in baglist:
        # print(val)
        baglist2 = find_bag(val, dict)
        bags |= set(baglist2)
    return bags


path = "data/bags.txt"
groups = open_file(path)
complete_dict = get_components(groups)
count_all('shiny gold', complete_dict)
