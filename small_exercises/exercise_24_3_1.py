
def cnvrt_strin(i_hrs, i_mins):
    a = f'{i_hrs:02d}'
    b = f'{i_mins:02d}'
    output = f'{a}:{b}'
    return output

def time_of_day(i_time):
    
    
    if i_time == 0:
        hrs = 0
        mins = 0
    elif i_time > 0:
        if i_time > 1440:
            i_time = i_time % 1440
        hrs = i_time // 60
        mins = i_time % 60
    else:
        if abs(i_time) > 1440:
            i_time = abs(i_time) % 1440
        else:
            i_time = abs(i_time)
        hrs = 23 - i_time // 60

        if i_time % 60 == 0:
            mins = 0
        else:
            mins = 60 - (i_time % 60)
    print(cnvrt_strin(hrs, mins))
    return cnvrt_strin(hrs, mins)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True


