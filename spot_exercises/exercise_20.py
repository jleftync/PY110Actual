"""
return a dictionary with the number of each letter appearances in a string as the key and a list of the letters that appear
that many times as the value

synthesized rules:
just letters and numbers - remove non alphanum for analysis
case insensitive - lower case everything for analysis

data structures:
separated chars into list
list with all lowercase letters
list of tuple with string list of strings
dictionary zipped
"""
def get_char_count(i_string):
    f_list = list(i_string)
    s_list = [x.lower() for x in f_list if x.isalnum()]
    t_list = []
    f_set = set()
    
    for y in s_list:
        e = s_list.count(y)
        if not t_list:
            t_list.append((e, [y]))
            f_set.add(e)
        
        
        if s_list.count(y) not in f_set:
            t_list.append((e, [y]))
            f_set.add(e)
        else:
            for z in t_list:
                if z[0] == e and y not in z[1]:
                    z[1].append(y)
   

    f_dict = dict(t_list)
    
    print(f_dict)





get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}