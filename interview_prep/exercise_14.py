
def seven_eleven(f_integer):
    f_list = [c for c in range(f_integer) if (c / 11 == int(c/11) or c/7 == int(c/7))]
    return sum(f_list)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)