def merge_sets(lst1, lst2):
    out_set = lst1 + lst2
    out_set = set(out_set)
    return out_set


list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
def merge_sets(list1, list2):
    return set(list1) | set(list2)