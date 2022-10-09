inp_str = input()
inp = list(inp_str)
if "L" not in inp and "R" not in inp and "B" not in inp:
    print(inp_str)
else:
    password = []
    cursor_pos = 0
    for i in inp:
        if i == 'L':
            cursor_pos -= 1
        elif i == 'R':
            cursor_pos += 1
        elif i == 'B':
            cursor_pos -= 1
            password.pop(cursor_pos)
        else:
            password.insert(cursor_pos, i)
            cursor_pos += 1

    print("".join(password))

# for i in range(len(inp)):
#     if inp[i] == 'L':
#         cursor_pos -= 1
#     elif inp[i] == 'R':
#         cursor_pos += 1
#     elif inp[i] == 'B':
#         cursor_pos -= 1
#         password.pop(cursor_pos)
