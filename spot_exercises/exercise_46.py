def triple_double(f_int, s_int):
    f_set = set(list(str(f_int)) + list(str(f_int)))
    f_str = str(f_int)
    s_str = str(s_int)
    for x in f_set:
        a = 3 * x
        b = 2 * x
        if a in f_str and b in s_str:
            print(1)
            return 1
    print(0)
    return 0



triple_double(12345, 12345)
triple_double(666789, 12345667)