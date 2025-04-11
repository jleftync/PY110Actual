def title_case(i_string, op_string=None):
    f_list = i_string.split()
    if op_string:
        t_list = op_string.split()
        t_list = [x.lower() for x in t_list]
    else:
        t_list = []
    s_list = []
    for idx, y in enumerate(f_list):
        if y.lower() not in t_list or idx == 0:
            z = y.capitalize()
            
            s_list.append(z)
        else:
            s_list.append(y.lower())


    print(" ".join(s_list))









title_case('a clash of KINGS', 'a an the of') # should return 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return 'The Wind in the Willows'
title_case('the quick brown fox') # should return 'The Quick Brown Fox'