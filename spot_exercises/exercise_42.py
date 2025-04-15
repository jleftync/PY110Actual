def find_children(i_string):
     f_list = sorted(list(i_string.lower()))
     f_set = set(f_list)
     s_list = [(x*f_list.count(x)).capitalize() for x in f_set]
     print("".join(s_list))


find_children("abBA") == "AaBb"
find_children("AaaaaZazzz") == "AaaaaaZzzz"
find_children("CbcBcbaA") == "AaBbbCcc"
find_children("xXfuUuuF") == "FfUuuuXx"
find_children("") == ""