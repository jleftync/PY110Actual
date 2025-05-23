def merge(a, b):
    c = a + b
    print(c)
    d = []
    while c:
        for x in c:
            if x == min(c):
                d.append(x)
                c.pop(c.index(x))
    return d
d = []

    

def merge_sort(y):
    if len(y) == 1:
        return y
    sub_list1 = y[:len(y)//2]
    sub_list2 = y[len(y)//2:]
    sub_list1 = merge_sort(sub_list1)
    sub_list2 = merge_sort(sub_list2)
    return merge(sub_list1, sub_list2)


 

print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)