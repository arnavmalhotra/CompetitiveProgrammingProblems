n = int(input())
strengthTeams = input().split()
print(strengthTeams)

totalMatches = (n*(n-1))/2
teamA = 0
teamB =0
totalRevenue = 0
absoluteDifference = 0

while teamA>=teamB:
    for num in range(0,n):
        if teamA != teamB:
            absoluteDifference = abs(int(strengthTeams[teamA])-int(strengthTeams[teamB]))
        else: 
            absoluteDifference = 0
        totalRevenue+=absoluteDifference
        teamB+=1
        print(num, teamA,teamB,totalRevenue)
    print("This is outer loop")
    print(num, teamA,teamB,totalRevenue)

    teamB = 0
    teamA+=1

print(totalRevenue)

# 3 10 3 5