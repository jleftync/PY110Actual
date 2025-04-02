def staggered_case(i_str):
    if i_str == "":
        return ""
    i_list = list(i_str)
    out_list = []
    out_str = ""
    for x in range(len(i_list)):
        if (x % 2) == 0:
            out_list.append(i_list[x].upper())
        else:
            out_list.append(i_list[x].lower())
    for y in range(len(out_list)):
        out_str = out_str + out_list[y]
    return out_str
    
        

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")         