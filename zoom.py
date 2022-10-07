leng = int(int(input())/2)
print(len)
input = input().split()
exists = False
outputs = [[0 for i in range(int(len(input)))] for j in range(int(leng))]


for every_other in range(1, leng, 1):
    for i in range(every_other-1, len(input), every_other):
        outputs[every_other][i] = int(input[i])
# for every_other in range(1, leng, 1):
#     for i in range(every_other-1, len(input), every_other):
#         if outputs[every_other][i] == 0:
#             outputs.pop(outputs[every_other][i])
list(filter(lambda a: a != 0, outputs))
print(outputs)
#     if(input[i+1]>input[i]):
#         print(input[i])
#         exists = True
# if(exists == False):
#     print("ABORT!")

# data0 = input()
# data1 = input()
# every_other = data0.split()
# every_other = int(every_other[1])
# data = data1.split()
# answer = []
# for i in range(every_other-1, len(data), every_other):
#     answer.append(data[i])
# for i in answer:
#     print(i+" ", end="")