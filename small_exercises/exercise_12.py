DEGREE = "\u00B0"

#(x//10000 * 60. x//100 * 60))
def dms(intgr):
    a = intgr // 1
    b = ((intgr - int(intgr)) * 60) // 1
    c = (intgr - int(intgr)) * 60
    d = (c - int(c)) * 60

    if b >= 10 and d >= 10:
        output = str(int(a)) + "\u00B0" + str(int(b)) + "'" + str(int(d)) + "\""
    elif b >= 10 and d < 10:
        output = str(int(a)) + "\u00B0" + str(int(b)) + "'0" + str(int(d)) + "\""
    elif b < 10 and d >= 10:
        output = str(int(a)) + "\u00B0" + "0" + str(int(b)) + "'" + str(int(d)) + "\""
    else:
        output = str(int(a)) + "\u00B0" + "0" + str(int(b)) + "'0" + str(int(d)) + "\""
    print(output)
    return output

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")