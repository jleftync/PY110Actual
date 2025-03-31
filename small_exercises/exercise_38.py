def substrings(i_str):
    i_list = list(i_str)
    print(i_str[1:])
    lst = []
    while i_list:
        lst.extend(["".join(i_list[:y+1]) for y in range(len(i_str))])
        i_list.pop(0)
        i_str = i_str[1:]
        
    return lst
    


print(substrings('abcde'))
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  