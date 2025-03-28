def helper(i_list):
    o_list = []

    while i_list:
        o_list.append(min(i_list))
        i_list.remove(min(i_list))
    
    return o_list

def create_dictionary(n_list, e_list):
    d_output = dict(zip(e_list, n_list))
    return d_output

def alphabetic_number_sort(num_list):
    en_list = ["zero", "one", "two", "three", "four", 
               "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
                 "thirteen", "fourteen", "fifteen", "sixteen", 
                 "seventeen", "eighteen", "nineteen"]
    w_n_dict = create_dictionary(num_list, en_list)
    
    
    en_list = helper(en_list)
    out_list = [w_n_dict[x] for x in en_list]
    return out_list

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)