inp = input()
tablet = 0
compass = 0
gear = 0
symbols = 0
for i in inp:
    if i == "T":
        tablet += 1
    elif i == "C":
        compass += 1
    elif i == "G":
        gear += 1
print(min(tablet, compass, gear)*7 + tablet**2 + compass**2 + gear**2)
