def delete_digit(i_string):
    f_list = list(str(i_string))
    max_list = []
    for idx, x in enumerate(f_list):
        max_list.append(int("".join(f_list[0:idx] + f_list[idx+1:])))
    print(max(max_list))



delete_digit(152)
delete_digit(1001)
delete_digit(10)