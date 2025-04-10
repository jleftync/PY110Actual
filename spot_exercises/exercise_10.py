def domain_name(i_str):
    f_list = i_str.split("/")
    s_list = [x.split(".") for x in f_list]
    t_list = [b for a in s_list for b in a]
    for idx, word in enumerate(t_list):
        if word == 'com':
            return t_list[idx-1]


domain_name("http://github.com/carbonfive/raygun") # should return "github"
domain_name("https://www.cnet.com") # should return "cnet"