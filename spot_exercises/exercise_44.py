def comp(f_list, s_list):
    if f_list == None or len(f_list) != len(s_list):
        print(False)
        return False
    t_list = sorted(f_list)
    fo_list = sorted(s_list)
    fi_list = [x ** 2 for x in t_list]
    if fo_list == fi_list:
        print(True)
        return True
    else:
        print(False)
        return False



comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True
comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False
comp(None, [1, 2, 3]) == False
comp([1, 2], []) == False
comp([1, 2], [1, 4, 4]) == False