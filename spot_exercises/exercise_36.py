def greatest_product(fi_string):
    mux_list = []
    max_list = []
    for x in range(len(fi_string) - 4):
        mux_list.append(list(fi_string[x:x+5]))
    
    for y in mux_list:
        var = 1
        for x in y:
            var *= int(x)
        max_list.append(var)
    print(max(max_list))

    
    


greatest_product("123834539327238239583") == 3240
greatest_product("395831238345393272382") == 3240
greatest_product("92494737828244222221111111532909999") == 5292
greatest_product("92494737828244222221111111532909999") == 5292
greatest_product("02494037820244202221011110532909999") == 0
