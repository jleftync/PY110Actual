def song_decoder(i_str):
    f_list = i_str.split("WUB")
    f_list = [x for x in f_list if x]
    print(" ".join(f_list))




song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")