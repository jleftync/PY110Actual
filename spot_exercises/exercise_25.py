def cakes(f_dict, s_dict):
    f_list = []
    for x in f_dict.keys():
        if x not in s_dict.keys() or f_dict[x] > s_dict[x]:
            
            return 0
        else: 
            f_list.append(s_dict[x] // f_dict[x])
            
    
    return min(f_list)

cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})

