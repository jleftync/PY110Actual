def solve(i_str):
    odd_sub = []
    
    for idx, x in enumerate(list(i_str)):
        counter = 1
        while True:
            if (idx + counter) > len(i_str):
                break
            elif int(i_str[idx:idx + counter]) % 2 != 0:
                odd_sub.append(int(i_str[idx:idx + counter]))
                counter += 1
            else: 
                counter += 1
        
    print(len(odd_sub))
            
            



solve("1341") # should return 7
solve("1357")