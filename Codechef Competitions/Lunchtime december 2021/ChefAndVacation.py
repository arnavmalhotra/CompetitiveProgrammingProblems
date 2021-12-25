n = int(input())
for num in range(n):
    x,y,z = input().split()
    if x+y<z:
        print("PLANEBUS")
    elif x+y>z:
        print("TRAIN")
    elif x+y==z:
        print("EQUAL")