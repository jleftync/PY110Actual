def scramble_help(inpt):
    scr_list = list(inpt)

    non_int_lst = [(idx, char) for idx, char in enumerate(scr_list) if not char.isalnum()]
    
    # Keep only alphanumeric characters in scr_list
    out_list = [char for char in scr_list if char.isalnum()]
    
    first, middle, last = out_list[0], out_list[1: -1], out_list[-1]
    middle.sort()
    mixed = [first] + middle + [last]
    for x, y in non_int_lst:
        mixed.insert(x, y)
    
    
    return("".join(mixed))

    
def scramble_words(in_str):
    
    if " " not in in_str:
        return scramble_help(in_str)
    
        
    lst = []
    out_str = []
    lst = in_str.split()
    for y in lst:
        out_str.append(scramble_help(y))
        
        
    
    return " ".join(out_str)

print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.")) # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")