
def persistence(i_int):
    counter = 0
    while i_int > 9:
        counter += 1
        y = 1
        z = list(str(i_int))
        for x in z:
            y *= int(x)
        i_int = y
    print(counter)


persistence(39) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit
persistence(999) # should return 4, because 9*9*9=729, 7*2*9=126,
# 1*2*6=12, and finally 1*2=2
persistence(4) # should return 0, because 4 is already a one-digit number
persistence(25) # should return 2, because 2*5=10, and 1*0=0