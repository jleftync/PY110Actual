def count_letters(in_string):
    lower_list = [sub for sub in in_string if sub.islower() == True]
    lower_in = "".join(lower_list)
    letter_set = set(lower_in)
    letter_set = {c for c in letter_set if c.isalpha()==True}
    print(letter_set)
    if not letter_set:
        return {}
    out_dict = {chr: lower_in.count(chr) for chr in letter_set}
    print(out_dict)
    return out_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})