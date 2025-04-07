def sum_square_difference(a):
    lst = [x + 1 for x in range(a)]
    return sum(lst) ** 2 - sum([y ** 2 for y in lst])



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True