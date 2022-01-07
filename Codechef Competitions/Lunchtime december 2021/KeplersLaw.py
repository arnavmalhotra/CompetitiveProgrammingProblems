n = int(input())
for num in range(n):
    numbers = list(map(int, input().split()))
    tp1 = numbers[0]*numbers[0]
    tp2 = numbers[1]*numbers[1]
    semiaxis = numbers[2]*numbers[2]*numbers[2]
    semiaxis2 = numbers[3]*numbers[3]*numbers[3]
    if tp1/semiaxis == tp2/semiaxis2 :
        print("Yes")
    else:
        print("no")
