n = int(input())
ans = 0
for i in range(0, n+1):
    j = n - i
    if(i % 5 == 0 and j % 4 == 0):
        ans = ans+1

print(ans)