def repeated_substring(i_string):
    f_list = []
    for i in range(len(i_string)):
        for j in range(1, len(i_string)+1):
            if i_string[i:j]:
                f_list.append(i_string[i:j])
    mult_list = [f for f in f_list if f * i_string.count(f) == i_string]
    mult_set_ls = list(set(mult_list))
    mult_set_ls = sorted(mult_set_ls, key=lambda mult: mult_list.count(mult), reverse=True)
    return (mult_set_ls[0], f_list.count(mult_set_ls[0]))

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))