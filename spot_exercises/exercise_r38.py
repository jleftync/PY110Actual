
def clean_string(f_string):
    f_list = list(f_string)
    
    o_list = []
    for x in f_list:
        if x == "#":
            if o_list:
                o_list.pop(-1)
        else:
            o_list.append(x)
    print("".join(o_list))
    
        

clean_string('abc#d##c')
clean_string('abc####d##c#')