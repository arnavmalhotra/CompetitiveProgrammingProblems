#TOW
cases = int(input())
for num in range(cases):
    players = []
    teamCounter = 0
    teamSize1 , teamSize2 = input().split()
    teamStrength = list(map(int,input().split()))
    opponentStrength = list(map(int,input().split()))
    teamSize1 , teamSize2  = int(teamSize1) , int(teamSize1)
    if sum(teamStrength)> sum(opponentStrength):
        print("YES")
        if teamStrength[teamCounter] < opponentStrength[num]:
            teamCounter+=1
        elif teamStrength[teamCounter] >= opponentStrength[num]:
            players.append(teamStrength[teamCounter])
        print(players , sep=" ")
    else:
        print("NO")

