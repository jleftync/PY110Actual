
def even_substrings(fi_string):
    out_list = []
    fi_list = list(fi_string)
    for idx, sub in enumerate(fi_list):
        while fi_list:
            for x in range(len(fi_list)+1):
                out_list.append("".join(fi_list[idx:x]))
            fi_list.pop(0)
    out_list = [int(char) for char in out_list if char]
    return sum(1 for b in out_list if b % 2 == 0)


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)