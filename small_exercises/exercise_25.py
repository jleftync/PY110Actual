hours_mins = 60

def compute_mins(i_hours, i_mins):
    x = (hours_mins * i_hours) + i_mins
    return x

def str_to_int(i_str):
    o_hours = int(i_str[0:2])
    o_mins = int(i_str[3:5])
    y = compute_mins(o_hours, o_mins)
    return y

def after_midnight(time):
    if time == "00:00" or time == "24:00":
        return 0
    else:
        return str_to_int(time)

def before_midnight(time):
    if time == "00:00":
        return 0
    else:
        return 1440 - (str_to_int(time))








print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True