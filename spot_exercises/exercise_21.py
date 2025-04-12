"""

problem: matrix math check for the one and  return the coordinates
data structures:  we can use comprehensions to iterate through
we will need two variables and an output list

synthesized rule: no matter what, the output variable list will be equal to the index

1. Create a function that receives a list of lists.
2.  Use enumerate function to scan iterate throuugh the outer list
3.  if 1 is detected within the list inside the list, set the first variable to the index of that
    function and iterate through the function inside of it
5.  use enumerate to iterate through the internal function where one is located
and set the second value to the value of the index where 1 is found.
6.  Return the two variables as a list

"""

def mine_location(i_str):
    a = 0
    b = 0
    for idx, x in enumerate(i_str):
        if 1 in x:
            a = idx
        for ind, y in enumerate(i_str[idx]):
            if y == 1:
                b = ind
    print ([a,b])






mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) # should return [1, 1]
mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) # should return [2, 1]
mine_location([[1, 0], [0, 0]]) # should return [0, 0]
mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) 