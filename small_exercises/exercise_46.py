def multiply_items(list_1, list_2):
    return [list_1[x] * list_2[x] for x in range(len(list_1))]





list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18])