import copy
def wave(i_str):
    if wave == "":
        return ""
    o_list = []
    f_list = list(i_str)
    for idx, x in enumerate(f_list):
        u_list = copy.deepcopy(f_list)
        if u_list[idx].isalpha() == True:
            u_list[idx] = u_list[idx].upper()
            o_list.append("".join(u_list))
    print(o_list)


            
            




wave("hello")
wave("")
wave("two words")
wave(" gap ")