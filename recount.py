from collections import Counter
inp = '''Penny Franklin
Connie Froggatt
Barbara Skinner
Connie Froggatt
Jose Antonio Gomez-Iglesias
Connie Froggatt
Bruce Stanger
Barbara Skinner
Barbara Skinner
***'''
names = inp.splitlines()
hMap = Counter(names)
currMax = -1
currWinner = ""
for key, val in hMap.items():
    if val > currMax:
        currMax = val
        currWinner = key
print(hMap)
# Checks if there are multiple winners
timesSeen = 0
for val in hMap.values():
    if val == currMax:
        timesSeen += 1
        if timesSeen > 1:
            print("Runoff!")
            exit()
print(currWinner)
