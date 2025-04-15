def dig_pow(f_int, s_int):
    f_list = list(str(f_int))
    s_list = [x + s_int for x in range(len(f_list))]
    t_list = [int(y) ** s_list[idx] for idx,y in enumerate(f_list)]
    x = sum(t_list)/f_int
    if x - int(x) != 0:
        print(-1)
    else:
        print(int(x))

dig_pow(89, 1) == 1
dig_pow(92, 1) == -1
dig_pow(46288, 3) == 51
dig_pow(695, 2) == 2