def average(i_list):
    x = i_list[0]
    for y in i_list[1:]:
        x += y
    z = x // len(i_list)
    return z

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)

def average(i_list):
    return sum(i_list) // len(i_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)