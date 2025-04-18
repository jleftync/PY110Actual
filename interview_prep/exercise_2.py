def minimum_sum(num_list):
    if len(num_list) < 5:
        return None
    five_sum = [sum(num_list[idx:idx+5]) for idx in range(len(num_list)-4)]
    print(min(five_sum))
    return min(five_sum)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)