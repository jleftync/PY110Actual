def order_by_value(i_dict):
    val_list = [x for x in i_dict.values()]
    val_list.sort()
    rev_dict = {v: k for k, v in i_dict.items()}
    output = [rev_dict[x] for x in val_list]
    return output


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys) 