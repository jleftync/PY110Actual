def interleave(inpt1, inpt2):
    output_lst = []
    for x in range(len(list1)):
        output_lst.append(list1[x])
        output_lst.append(list2[x])
    return output_lst




list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)