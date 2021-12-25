n = int(input())
for num in range(n):
    x,y,z = input().split()
    x,y,z = int(x), int(y) , int(z)
    if x+y<z:
        print("PLANEBUS")
    elif x+y>z:
        print("TRAIN")
    elif x+y==z:
        print("EQUAL")