
def is_valid_walk(i_string):
    counter_ns = 0
    counter_ew = 0
    for x in i_string:
        if x == 'n':
            counter_ns += 1
        if x == 's':
            counter_ns -= 1
        if x == 'w':
            counter_ew -= 1
        if x == 'e':
            counter_ew += 1
    if counter_ns == 0 and counter_ew == 0 and len(i_string) == 10:
        print(True)
        return True
    else:
        print(False)
        return False

is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
is_valid_walk(['w']) # should return False
is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return F