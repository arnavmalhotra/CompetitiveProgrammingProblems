n = int(input())
for num in range(n):
    num = int(input())
    print(sum(sorted(list(map(int,(input().split()))))[1:]))