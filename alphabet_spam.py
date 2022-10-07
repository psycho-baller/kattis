inp = input()
wht_spc = 0
lower = 0
upper = 0
symbols = 0
for i in inp:
    if i == "_":
        wht_spc += 1
    elif (97 <= ord(i) <= 122):
        lower += 1
    elif (65 <= ord(i) <= 90):
        upper+=1
    else:
        symbols+=1
len_inp = len(inp)
print(wht_spc/len_inp)
print(lower/len_inp)
print(upper/len_inp)
print(symbols/len_inp)
