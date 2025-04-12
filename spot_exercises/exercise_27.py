def anagrams(f_str, s_str):
    t_list = []
    for b in s_str:
        
        for x in b:
            if f_str.count(x) != b.count(x):
                break
            elif b not in t_list:
                t_list.append(b)
    print(t_list)

    


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])