def minimum_number(i_list):
    x = sum(i_list)
    counter = 1
    
    while counter:
        y = x
        y -= 1
        y += counter
        z = [a for a in range(x, y+1)]
        h = [b/c for b in z for c in range(2, y) if type(b) == int]
        if bool(h) == False:
            i = y-x
            print(i)
            return i
            

minimum_number([3,1,2])
minimum_number([5,2])
minimum_number([1,1,1])
minimum_number([2,12,8,4,6])
minimum_number([50,39,49,6,17,28])