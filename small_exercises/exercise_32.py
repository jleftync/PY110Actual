def reverse_list(i_lst):
    z = []
    if i_lst == []:
        return i_lst
    while i_lst:
        z.append(i_lst.pop())
    while z:
        i_lst.append(z.pop(0))
    return i_lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])
print(list1)               # True
print(list1 is result)                      # True
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True