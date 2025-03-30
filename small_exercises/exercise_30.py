def swap_name(i_str):
    i_lst = i_str.split()
    print(i_lst)
    out_str = f"{i_lst[1]}, {i_lst[0]}"
    print(out_str)
    return out_str
    
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True