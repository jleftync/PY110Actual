def helper(in_set, o_list):
    y = o_list.count(in_set)
    r_string = f"{in_set} => {y}"
    print(r_string)

def count_occurrences(i_list):
    i_set = set(i_list)
    for x in i_set:
        helper(x, i_list)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

def count_occurrences(i_list):
    i_set = set(i_list)
    [print(f"{x} => {y}") for x in i_set if (y := i_list.count(x))]

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)