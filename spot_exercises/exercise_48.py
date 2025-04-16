
def reverse_and_combine_text(f_string):
    if " " not in f_string:
        print(f_string)
        return f_string
    f_list = f_string.split()
    s_list = ["".join(sorted(list(x))[::-1]) for x in f_list]
    print("".join(s_list))

reverse_and_combine_text("abc def")
reverse_and_combine_text("abc def ghi jkl")
reverse_and_combine_text("dfghrtcbafed")
reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44")
reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt")