

def nearest_prime_sum(i_list):
    si = sum(i_list)
    counter = 1
    while True:
        
        so = si + counter
        for x in range(2, int(so ** .5) + 1):
            if so % 3 == 0:
                counter += 1
                break
            if so % 3 ==0:
                counter += 1
                break
            if so % x == 0:
                counter += 1
                break
            
        else:
            return so - si



print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)