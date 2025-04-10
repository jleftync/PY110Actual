def top_3_words(i_string):
    i_list = i_string.split()
    n_list = [x.split("-") for x in i_list]
    o_list = [y for z in n_list for y in z]
    
    p_list = []
    for d in o_list:
        a = ""
        for e in d:
            if e.isalpha():
                a += e
        if a:
            p_list.append(a)
    
    o_set = {(p_list.count(e), e) for e in p_list}
    o_list = list(o_set)
    o_list.sort()
    o_list.reverse()
    if len(o_list) < 3:
        print([s[1] for s in o_list])
        return [s[1] for s in o_list]
    else:
        
        return [s[1] for s in o_list[0: 3]]

top_3_words("n a village of La Mancha, the name of which I have no desire to call to")