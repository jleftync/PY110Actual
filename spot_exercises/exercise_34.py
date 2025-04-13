import copy
pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

def find_suspects(f_dict, f_list):
    s_list = []

    s_dict = copy.deepcopy(f_dict)
     
    for x in f_list:
        for y in s_dict.keys():
            if x in s_dict[y]:
                s_dict[y].remove(x)
    
    for x in s_dict.keys():
        if s_dict[x] != []:
            s_list.append(x)
    print(s_list)
    
                
    


find_suspects(pockets, [1, 2])
find_suspects(pockets, [1, 7, 5, 2])
find_suspects(pockets, [])
find_suspects(pockets, [7])