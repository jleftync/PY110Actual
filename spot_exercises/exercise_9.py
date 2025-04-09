def scramble_help(inpt):
    scr_list = list(inpt)
    
    
    # Filter out non-alphanumeric characters and store their original positions
    non_int_lst = [(idx, char) for idx, char in enumerate(scr_list) if not char.isalnum()]
    
    # Keep only alphanumeric characters in scr_list
    out_list = [char for char in scr_list if char.isalnum()]
    first_and_last = [scr_list.pop(0),  scr_list.pop()]
    
    # Sort the remaining characters
    out_list.sort()
    

    for idx, char in non_int_lst:
        scr_list.insert(idx, char)
        
    print(f"{first_and_last[0]}" +"".join(scr_list) + f"{first_and_last[1]}")

    return f"{first_and_last[0]}" +"".join(scr_list) + f"{first_and_last[1]}"

    
    
def scramble_words(in_str):
    
    if " " not in in_str:
        return scramble_help(in_str)
    
        
    lst = []
    out_str = []
    lst = in_str.split()
    for y in lst:
        out_str.append(scramble_help(y))
        
        
    
    return " ".join(lst)
