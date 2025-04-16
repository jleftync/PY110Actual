def find_missing_letter(i_list):
    f_list = [x for x in range(ord(i_list[0]), ord(i_list[-1]) + 1)]
    s_list = [chr(y) for y in f_list]
    for z in s_list:
        if z not in i_list:
            print(z)
            return z


find_missing_letter(['a','b','c','d','f'])
find_missing_letter(['O','Q','R','S'])