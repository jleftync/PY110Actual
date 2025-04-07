def bubble_sort(i_lst):
    
    while True:
        counter = 0
        for idx, x in enumerate(i_lst[:-1]):
            if i_lst[idx] > i_lst[idx+1]:
                i_lst[idx], i_lst[idx+1] = i_lst[idx+1], i_lst[idx]
                counter += 1
        if counter == 0:
            return i_lst
        
        
        


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)        