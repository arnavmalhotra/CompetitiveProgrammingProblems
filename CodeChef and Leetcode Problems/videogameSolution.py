dimensions = input().split()
initial = input().split()
commands = input().split()

current = 0
occupied = False

for command in commands:
    if int(command) == 0:
        print (' '.join(initial))
        break
    elif int(command) == 1:
        if current != 0:
            current = current - 1
    elif int(command) == 2:
        if current != int(dimensions[0])-1 :
            current = current + 1
    elif int(command) == 3:
        if not occupied:
            if int(initial[current]) != 0:
                occupied = True
                initial[current] = str(int(initial[current]) - 1)
    elif int(command) == 4:
        if occupied:
            if int(initial[current]) != int(dimensions[1]):
                occupied = False
                initial[current] = str(int(initial[current]) + 1)
