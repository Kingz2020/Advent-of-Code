import pandas as pd


def open_file(path):
    """Opens a file and returns the list of groups"""
    with open(path, 'r') as f:
        groups = f.read().split('\n')
    return groups


def find_child(parent_bag):
    """ """
    content = bags_dict[parent_bag].split(", ")
    if content[0] == "no other":
        return
    else:
        for child in content:
            bagname = child[2:]
            number = int(child[0])
            if bagname in child_count:
                child_count[bagname] += number
            else:
                child_count[bagname] = number
            for i in range(number):
                find_child(bagname)
        return


path = "data/bags.txt"
bags = open_file(path)
bags_dict = {}
for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")
    bag = bag.split(" contain ")
    bags_dict[bag[0]] = bag[1]
child_count = {}
find_child("shiny gold")
print("Part 2: Total number of bags: " + str(sum(child_count.values())))
