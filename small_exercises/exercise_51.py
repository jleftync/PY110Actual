def unique_sequence(i_list):
    output = []
    for x in i_list:
        if x not in output:
            output.append(x)
    return output
    


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)