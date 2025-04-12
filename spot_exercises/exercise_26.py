def solution(f_list, s_list):
    t_list = [(s_list[idx] - x) ** 2 for idx, x in enumerate(f_list)]
    print(sum(t_list)/len(t_list))
              
    
    
solution([1, 2, 3], [4, 5, 6]) == 9
solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5
solution([-1, 0], [0, -1]) == 1