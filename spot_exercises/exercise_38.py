
def duplicate_encode(f_string):
    s_string = ""
    for x in f_string.lower():
        if f_string.lower().count(x) == 1:
            s_string += "("
        else:
            s_string += ")"
    print(s_string)
        
            

duplicate_encode("din")
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")