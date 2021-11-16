# manipulate arrays
# 1: move left if not leftmost
# 2: move right if not rightmost
# 3: pick up if there is a box
# 4: drop if not max height
# 0:quit 

#INCORRECT (Array does not get updated)

dimensions = input().split()
initialBoxes = input().split()
commands = input().split()

current =0
occupied = False

for command in commands:
    if command==1:
        if current!=0:
            print(' '.join(initialBoxes))
    elif command==1:
        if current!=0:
            current-=1
    elif command==2:
        if current!=int(dimensions[0]):
            current-+1
    elif command==3:
        if not occupied:
            if str(initialBoxes[current])!=0:
                initialBoxes[current] = str(int(initialBoxes[current]))-1
    elif command ==4:
        if occupied:
            if str(initialBoxes[current])!=int(dimensions[current]):
                initialBoxes[current] = str(int(initialBoxes[current]))+1
print(initialBoxes)