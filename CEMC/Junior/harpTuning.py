import re
instructions = input()
for character in instructions:
    previous = instructions.index(character)-1
    if instructions[previous].isnumeric() and character.isalpha() and previous!=-1:
        print("")
    if character =="+":
        print(" tighten ", end='')
    elif character =="-":
        print(" loosen ", end='')
    else:
        print(character, end='')
