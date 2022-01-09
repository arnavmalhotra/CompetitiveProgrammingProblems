testCases = int(input())
for num in range(testCases):
    playersBetween , correctHeight = input().split()
    heights = list(map(int, input().split()))
    killCount = 0
    for num in heights:
        if num > int(correctHeight):
            killCount +=1
    print(killCount)