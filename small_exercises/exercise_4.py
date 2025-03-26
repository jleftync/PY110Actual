def running_total(inpt):
    output_list = []
    y = inpt[0]
    output_list.append(y)
    for x in range(len(inpt[1:])):
        y += inpt[x + 1]
        output_list.append(y) 
    return output_list

print(running_total([2, 5, 13]))    # True