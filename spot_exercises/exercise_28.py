def solution(i_str):
    if not i_str:
        return []
    x = list(i_str)
    if len(i_str) % 2 == 0:
        z = [y + x[idx+1] for idx, y in enumerate(x[::2])]
    else:
        z = [y + x[idx+1] for idx, y in enumerate(x[:-1:2])]
        z.append(f"{x[-1]}_")
    print(z)
    

solution('abc')
solution('abcdef')
solution("abcdef") 
solution("abcdefg")
solution("")