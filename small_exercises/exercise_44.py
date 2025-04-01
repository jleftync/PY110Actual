def remove_vowels(i_lst):
    out_lst = []
    for z in range(len(i_lst)):        
        lst_a = list(i_lst[z])
        lst_a = [lst_a[x] for x in range(len(lst_a)) if lst_a[x].lower() not in 'aeiou']
        y = "".join(lst_a[:])
        out_lst.append(y)
    return out_lst
    


original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)