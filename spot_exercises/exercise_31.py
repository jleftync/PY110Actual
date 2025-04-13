


def high(i_string):
    f_list = i_string.split()
    s_list = [list(x) for x in f_list]
    t_list = [sum([ord(z) - 96 for z in y]) for y in s_list]
    print(t_list)
    fo_list = list(zip(t_list, f_list))
    print(max(fo_list)[1])
    




high('man i need a taxi up to ubud')
high('what time are we climbing up the volcano')
high('take me to semynak')
high('aaa b')