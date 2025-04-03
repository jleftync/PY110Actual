
def minilang(inpt):
    stcklst = []
    n = 0
    lst_inpt = inpt.split()
    
    for x in lst_inpt:
        if x.lstrip('-').isdigit():
            n = int(x)
        if x == 'PUSH':
            stcklst.append(n)
            
        if x == 'PRINT':
            print(abs(n))
        if x == 'POP':
            n = stcklst.pop()
        if x == 'ADD':
            n = n + stcklst[-1]
            stcklst.pop()
        if x == 'SUB':
            n = n - stcklst[-1]
            stcklst.pop()
        if x == 'MULT':
            n = n * stcklst[-1]
            stcklst.pop()
        if x == 'DIV':
            n = n // stcklst[-1]
            
            stcklst.pop()
        if x == 'REMAINDER':
            n = n % stcklst[-1]
            stcklst.pop()
        
        

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')

"""

n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value."
"""