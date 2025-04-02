def unique_sequence(i_list):
    output = []
    for idx, x in enumerate(i_list):
        if idx == 0 or x != i_list[idx-1]:
            output.append(x)
    return output
    


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)