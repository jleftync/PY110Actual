
def binary_search(inpt, s_term, offset = 0):
    mid = len(inpt)//2
    if not inpt:
        return -1 
    if inpt[mid] == s_term:
       
        return offset + mid
    if inpt[mid] < s_term:
        
        offset += mid + 1
        return binary_search(inpt[mid+1:], s_term, offset)


    if inpt[mid] > s_term:
        
        return binary_search(inpt[:mid], s_term, offset) 






businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)