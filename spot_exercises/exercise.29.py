def anagram_difference(f_str, s_str):
    if not f_str and not s_str:
        print(0)
        return 0
    counter = 0
    if f_str == s_str or sorted(f_str) == sorted(s_str):
        print(0)
        return 0
    for x in f_str:
        if x not in s_str:
            counter += 1
    for y in set(f_str):
        if y in set(f_str) and y in s_str:
            counter += abs(f_str.count(y) - s_str.count(y))
    for z in s_str:
        if z not in f_str:
            counter += 1
    
    print(counter)


anagram_difference('', '')
anagram_difference('a', '')
anagram_difference('', 'a')
anagram_difference('ab', 'a')
anagram_difference('ab', 'ba')
anagram_difference('ab', 'cd')
anagram_difference('aab', 'a')
anagram_difference('a', 'aab')