inpu = '''13 50
____$$$_______$$$______$$$________$$$______$$$____
____$$$_______$$$______$$$________$$$______$$$____
_____$_________$________$__________$________$_____
___$_$_$_____$_$_$____$_$_$______$_$_$____$_$_$___
__$__$_$____$__$__$___$_$__$____$__$__$___$_$__$__
_$____$$____$__$__$___$$____$___$__$__$___$$____$_
$_____$$___$___$___$__$$_____$_$___$___$__$$_____$
_____$_$______$_$_____$_$_________$_$_____$_$_____
____$___$____$___$____$___$______$___$____$___$___
___$____$___$_____$___$____$____$_____$___$____$__
__$_____$___$_____$___$_____$___$_____$___$_____$_
__$_____$___$_____$___$_____$___$_____$___$_____$_
_$$_____$$_$$_____$$_$$_____$$_$$_____$$_$$_____$$

'''

inp = inpu.split("\n")
width = int(inp[0].split()[1])
line = list(inp[1])

rating = 0

i = 0
while i < width:
    if line[i] == "$":
        rating += 1
        while i < width and line[i] == "$":
            i += 1
    i += 1
print(rating)
