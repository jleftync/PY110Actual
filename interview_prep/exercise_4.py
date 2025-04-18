def closest_numbers(input_list):
    srt_list = sorted(input_list)
    diff_list = []
    for x in range(len(srt_list)-1):
        diff_list.append(abs(srt_list[x+1] - srt_list[x]))
    print(diff_list)
    x = diff_list.index(min(diff_list))
    y = (srt_list[x], srt_list[x + 1]) if input_list.index(srt_list[x]) < input_list.index(srt_list[x+1]) else (srt_list[x+1], srt_list[x])
    print(y)

    srt = sorted(input_list)
    pairs = list(zip(srt, srt[1:]))
    closest_pair = min(pairs, key=lambda pair: abs(pair[1] - pair[0]))
    
    # Reorder to match original input
    a, b = closest_pair
    return (a, b) if input_list.index(a) < input_list.index(b) else (b, a)


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))