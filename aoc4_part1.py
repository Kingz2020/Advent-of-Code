import pandas as pd


def break_line(lst):
    """Breaks a list into smallest components seprerated by space or \n."""
    new_list = []
    for element in range(len(lst)):
        new_list.extend(lst[element].split(' '))
    return new_list


def list_to_dict(sep, lst):
    """Converts list to dictionary."""
    mydict = {}
    for ele in range(len(lst)):
        pos = lst[ele].find(':')
        mydict[lst[ele][:pos]] = lst[ele][pos+1:]
    return mydict


def fill_valid(df):
    """Fills the column valid appropriately."""
    df['valid'] = 1
    for idx, row in df.iterrows():
        if pd.isnull(row['eyr']) |
        pd.isnull(row['byr']) |
        pd.isnull(row['iyr']) |
        pd.isnull(row['hgt']) |
        pd.isnull(row['hcl']) |
        pd.isnull(row['ecl']) |
        pd.isnull(row['pid']) |
        pd.isnull(row['hgt']):
            df['valid'][idx] = 0


def fill_valid2(df):
    """Fills the column valid according to the 2nd rule, 
    that cid can be empty aslong as noone else is"""
    for idx, row in df.iterrows():
        if pd.isnull(row['cid']) &
        (pd.isnull(row['byr']) |
         pd.isnull(row['iyr']) |
         pd.isnull(row['hgt']) |
         pd.isnull(row['hcl']) |
         pd.isnull(row['ecl']) |
         pd.isnull(row['pid']) |
         pd.isnull(row['hgt'])):
            df['valid'][idx] = 0


def do_it_all(path):
    """ gets the file, converts into a dictionary, converts the 
    dict to df and returns the dataframe"""
    df = pd.DataFrame(columns=['eyr', 'byr', 'iyr',
                               'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    with open(path, 'r') as f:
        identities = f.read().split('\n\n')
    for idx in range(len(identities)):
        word = identities[idx].split('\n')
        mydict = break_line(word)
        mydict = list_to_dict(':', mydict)
        temp_df = pd.DataFrame.from_dict({idx: mydict})
        temp_df = temp_df.T
        df = pd.concat([df, temp_df])
    return df


path = 'data/ids.txt'
df = do_it_all(path)
df.drop([''], axis=1, inplace=True)
fill_valid(df)
fill_valid2
answer = df['valid'].sum()

print(f'The answer is {answer}')  # 235
