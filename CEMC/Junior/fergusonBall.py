n = int(input())
starPlayers = 0
for num in range(n):
    points = int(input())
    fouls = int(input())
    stars = (points*5)-(fouls*3)
    if stars > 40:
        starPlayers +=1
if starPlayers == n:
    print(str(starPlayers)+"+")
else:
    print(starPlayers)