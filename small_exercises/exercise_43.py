def keep_keys(i_dict, i_keys):
    return {k: v for k,v in i_dict.items() if k in i_keys}






input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True