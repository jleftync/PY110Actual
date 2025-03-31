def unique_from_first(in_1, in_2):
    return set([x for x in in_1 if x not in in_2])




list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})