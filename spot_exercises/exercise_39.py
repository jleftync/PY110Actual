
def sortme(f_list):
    s_list = [x.lower() for x in f_list]
    t_list = sorted(list(zip(s_list, f_list)))
    fo_list = [x[1] for x in t_list]
    print(fo_list)

sortme(["Hello", "there", "I'm", "fine"])
sortme(["C", "d", "a", "Ba", "be"])