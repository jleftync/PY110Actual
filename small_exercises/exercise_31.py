def sequence(rnge, mux):
    if rnge == 0:
        return []
    else:
        return [(x+1) * mux for x in range(rnge)]





print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])      