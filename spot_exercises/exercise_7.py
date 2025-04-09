def f(i_str):
    counter = 1
    while True:
        if i_str[:counter] * int(len(i_str)/counter) == i_str:
            return [i_str[:counter], len(i_str)/counter]
        if len(i_str[:counter]) > len(i_str)/2:
            return [i_str, 1]
        

print(f("ababab"))# should 