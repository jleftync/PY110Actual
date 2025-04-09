x# x = 'xuz'
# print([x.index(y) for y in x])


alpha = 'abcdefghijklmnopqrstuvwxyz'
def index_helper(inpt):
    return len([inpt.index(y) for y in inpt if inpt.lower().index(y.lower()) == alpha.index(y.lower())])
print(alpha.index('a'))
def solve(i_lst):
    print([index_helper(x) for x in i_lst])

def index_helper(inpt):
    return sum(1 for i, ch in enumerate(inpt.lower()) if i < 26 and ch == alpha[i])

def solve(i_lst):
    print([index_helper(x) for x in i_lst])
    



solve(["abode","ABc","xyzD"]) # should return [4, 3, 1]
solve(["abide","ABc","xyz"]) # 