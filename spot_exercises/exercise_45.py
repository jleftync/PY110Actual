def group_and_count(i_list):
    if bool(i_list) == False:
        return None
    f_set = set(i_list)
    f_dict = {x: i_list.count(x) for x in f_set}
    print(f_dict)




group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1}
group_and_count([]) == None
group_and_count(None) == None
group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1}