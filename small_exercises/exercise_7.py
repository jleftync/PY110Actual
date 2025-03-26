def str_change(inpt):
    output_str = ""
    if len(inpt) == 1:
        output_str += inpt
        return output_str
    output_str += inpt[-1]
    output_str += inpt [1:-1]
    output_str += inpt[0]
    return output_str
def swap(strng):
    output = ""
    lst = strng.split()
    lst = [str_change(x) for x in lst]
    for y in lst:
        if len(lst) == 1:
            output += y
            return  output
        else:
            output += f"{y} "
        
            
    output = output[:-1]      
    return output


print(swap('Oh what a wonderful day it is'))
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")
print(swap('a'))  # True
print(swap('a') == "a")       