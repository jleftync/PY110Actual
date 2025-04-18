def closest_numbers(input_list):
    srt_list = sorted(input_list)
    diff_list = []
    for x in range(len(srt_list)-1):
        diff_list.append(abs(srt_list[x+1] - srt_list[x]))
    print(diff_list)
    x = diff_list.index(min(diff_list))
    y = (srt_list[x], srt_list[x + 1]) if input_list.index(srt_list[x]) < input_list.index(srt_list[x+1]) else (srt_list[x+1], srt_list[x])
    print(y)


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))