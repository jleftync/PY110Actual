def reverse_number(i_int):
    i = int(str(i_int)[::-1])
    print(i)
    return(i)


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True