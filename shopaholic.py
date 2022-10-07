length = int(input())
numbers = input().split()
numbers[:] = [int(num) for num in numbers]
numbers[:] = sorted(numbers, reverse=True)
save = 0
for i in range(length):
    if i%3 == 2:
        save+=numbers[i]

print(save)
