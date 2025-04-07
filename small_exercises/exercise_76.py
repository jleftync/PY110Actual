def triangle(a, b, c):
    if 0 in (a, b, c):
        return "invalid"
    elif (a + b + c) != 180:
        return "invalid"
    elif 90 in (a, b, c):
        return "right"
    elif a < 90 and b < 90 and c < 90:
        return "acute"
    else:
        return "obtuse"




print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True