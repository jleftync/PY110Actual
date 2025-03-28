def add_to(inpt_1, inpt_2):
    output_lst = []
    output_lst.append(inpt_1)
    output_lst.append(inpt_2)
    print(output_lst)
    return output_lst

def halvsies(lst_in):
    out_1 = []
    out_2 = []
    if lst_in == []:
        return [[], []]
    elif len(lst_in) == 1:
        return [lst_in, []]
    elif (len(lst_in) % 2) == 0:
        a = int(len(lst_in) / 2)
        out_1 = lst_in[0:a]
        out_2 = lst_in[a:]
        return add_to(out_1, out_2)
    else:
        b = int(len(lst_in)/2 + 1)
        out_1 = lst_in[0:b]
        out_2 = lst_in[b:]
        return add_to(out_1, out_2)




print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])