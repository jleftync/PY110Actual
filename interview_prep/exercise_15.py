def greatest_product(i_string):
    # i_list = list(i_string)
    # out = 1
    # out_list = []
    # for idx, num in enumerate(i_list):
    #     if idx + 4 <= len(i_list):
    #         for c in i_list[idx: idx+4]:
    #             out *= int(c)
    #         out_list.append(out)
    #         out = 1
    return max(int(i_string[i]) * int(i_string[i+1]) * int(i_string[i+2]) * int(i_string[i+3]) for i in range(len(i_string)-3))
    #for these situations, fuguring out range think about slicing and ask what last digit of slice would be
    

    


    


        
    print(out_list)
    return max(out_list)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6