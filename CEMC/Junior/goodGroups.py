x = int(input())
sameGroup = {}
for _ in range(x):
    a, b = input().split(' ')
    if(a not in sameGroup):
        sameGroup[a] = [b]
    else:
        sameGroup[a].append(b)


# print(sameGroup)
differentGroup = {}
y = int(input())
for _ in range(y):
    a, b = input().split(' ')
    if(a not in differentGroup):
        differentGroup[a] = [b]
    else:
        differentGroup[a].append(b)
    if(b not in differentGroup):
        differentGroup[b] = [a]
    else:
        differentGroup[b].append(a)


# print(differentGroup)
violated = 0
g = int(input())
for z in range(g):
    a, b, c = input().split(" ")

    for i in sameGroup.get(a, []):
        if i not in (b,c):
            violated += 1
    for i in sameGroup.get(b, []):
        if i not in (a,c):
            violated += 1
    for i in sameGroup.get(c, []):
        if i not in (a,b):
            violated += 1

    # print(z, violated)

    if a in differentGroup.get(b, []):
        violated = violated + 1
    if b in differentGroup.get(c, []):
        violated = violated + 1
    if c in differentGroup.get(a, []):
        violated = violated + 1

    # print(z, violated)

print(violated)