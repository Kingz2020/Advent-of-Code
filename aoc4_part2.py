import re


def check_eyr(df):
    """ checks eyr and sets column to 0 if conditions are not met"""
    df["eyr"] = pd.to_numeric(df["eyr"])
    df.loc[(df['eyr'] < 2020) | (df['eyr'] > 2030), 'valid'] = 0
    #print(df.loc[(df['eyr'] < 2020) | (df['eyr'] > 2030), 'valid'])
    df = df.reset_index(drop=True)
    print("check eyr completed & df updated")
    return df


def check_byr(df):
    """ checks eyr and sets column to 0 if conditions are not met"""
    df["byr"] = pd.to_numeric(df["byr"])
    df.loc[(df['byr'] < 1920) | (df['byr'] > 2002), 'valid'] = 0
    #print(df.loc[(df['byr'] < 1920) | (df['byr'] > 2002),'valid'])
    df = df.reset_index(drop=True)
    print("check byr completed & df updated")
    return df


def check_iyr(df):
    """ checks eyr and sets column to 0 if conditions are not met"""
    df["iyr"] = pd.to_numeric(df["iyr"])
    df.loc[(df['iyr'] < 2010) | (df['iyr'] > 2020), 'valid'] = 0

    df.drop(df[df['valid'] == 0].index, inplace=True)
    df = df.reset_index(drop=True)
    print("check iyr completed & df updated")
    return df


def check_hgt(df):
    """ checks eyr and sets column to 0 if conditions are not met"""
    for idx, row in df.iterrows():
        if row['hgt'][-2:] == 'cm':
            if (int(row['hgt'][:-2]) < 150) | (int(row['hgt'][:-2]) > 193):
                df['valid'][idx] = 0
        elif row['hgt'][-2:] == 'in':
            if (int(row['hgt'][:-2]) < 59) | (int(row['hgt'][:-2]) > 76):
                df['valid'][idx] = 0
        elif (row['hgt'][-2:] != 'cm') | (row['hgt'][-2:] != 'in'):
            df['valid'][idx] = 0
    df = df.reset_index(drop=True)
    print("check hgt completed & df updated")
    return df


def check_hcl(df):
    """"""
    for idx, row in df.iterrows():
        if (row['hcl'][:-6] != '#') | (len(row['hcl']) != 7) |
        (not re.match("^[a-f0-9]*$", row['hcl'][-6:])):
            first = row['hcl'][:-6]
            length = len(row['hcl'])
            code = row['hcl'][-6:]
            df['valid'][idx] = 0
    df = df.reset_index(drop=True)
    print("check hcl completed & df updated")
    return df


def check_ecl(df):
    """"""
    possibles = ['blu', 'amb', 'brn', 'grn', 'hzl', 'gry', 'oth']
    for idx, row in df.iterrows():
        if row['ecl'] not in possibles:
            df['valid'][idx] = 0
    df = df.reset_index(drop=True)
    print("check ecl completed & df updated")
    return df


def check_pid(df):
    """"""
    for idx, row in df.iterrows():
        if len(row['pid']) != 9:
            df['valid'][idx] = 0
    df = df.reset_index(drop=True)
    print("check pid completed & df updated")
    return df


def delete_non_valids(df):
    """"""
    print(f'shape 1: {df.shape}')
    df.drop(df[df['valid'] == 0].index, inplace=True)
    print(f'shape 2: {df.shape}')
    df = df.reset_index(drop=True)
    print("non-valid rows have been deleted")
    return df


def all_checks(df):
    """Performs all checks for part 2."""
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or no
    """
    df = check_eyr(df)
    df = delete_non_valids(df)
    df = check_byr(df)
    df = delete_non_valids(df)
    df = check_iyr(df)
    df = delete_non_valids(df)
    df = check_hgt(df)
    df = delete_non_valids(df)
    df = check_hcl(df)
    df = delete_non_valids(df)
    df = check_ecl(df)
    df = delete_non_valids(df)
    df = check_pid(df)
    df = delete_non_valids(df)
    return df


def do_it_all(path):
    """ gets the file, converts into a dictionary, converts the dict to df and returns the dataframe"""
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
        # print(df)
    return df


path = 'data/ids.txt'
df = do_it_all(path)
df.drop([''], axis=1, inplace=True)
df = fill_valid(df)
df = fill_valid2(df)
answer = df['valid'].sum()
print(f'The answer to part 1 is {answer}')
df.drop(df[df['valid'] == 0].index, inplace=True)
df = df.reset_index(drop=True)
print("ready for part 2")

df = all_checks(df)
answer = df['valid'].sum()
print(f'The answer to part 2 is {answer}')
