#do on computer

n = int(input())
for num in range(n):
    dsaSloth , tocSloth, dmSloth = input().split()
    dsaSloth, tocSloth, dmSloth = int(dsaSloth), int(tocSloth), int(dmSloth)
    dsaDragon , tocDragon, dmDragon = input().split()
    dsaDragon, tocDragon, dmDragon = int(dsaDragon), int(tocDragon), int(dmDragon)
    if dsaSloth > dsaDragon:
        print("DRAGON")
    elif dsaDragon>dsaSloth:
        print("SLOTH")
    elif tocSloth > tocDragon:
        print("DRAGON")
    elif tocDragon > tocSloth:
        print("SLOTH")
    else:
        print("TIE")