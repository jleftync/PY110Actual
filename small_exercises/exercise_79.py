def transpose(i_lst):
    
    print(list(zip(*i_lst)))
    return [[sub[i] for sub in i_lst] for i in range(len(i_lst))]

    
    


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True