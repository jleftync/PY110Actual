def spin_words(i_string):
    f_list = i_string.split()
    o_list = []
    for x in f_list:
        
        if len(x) < 5:
            o_list.append(x)
        else:
            a = list(x)
            a.reverse()
            o_list.append("".join(a))
    print(" ".join(o_list))
        
            



spin_words("Hey fellow warriors") # should return "Hey wollef sroirraw"
spin_words("This is a test") # should return "This is a test"
spin_words("This is another test") # 