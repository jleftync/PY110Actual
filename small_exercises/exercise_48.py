def sum_digits(in_num):
    x = list(str(in_num))
    y = sum([int(z) for z in x])
    return y


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)