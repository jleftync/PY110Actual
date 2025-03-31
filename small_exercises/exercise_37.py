def leading_substrings(i_str):
    i_list = list(i_str)
    return ["".join(i_list[:y+1]) for y in range(len(i_str))]

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])