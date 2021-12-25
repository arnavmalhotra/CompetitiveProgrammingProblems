for num in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    x = sorted(x)
    has = (x[-1]-x[0])*x[-2]
    print(has)