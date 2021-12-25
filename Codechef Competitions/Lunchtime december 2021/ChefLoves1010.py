for n in range(int(input())):
    length = int(input())
    string = input()
    count1 = string.count('1')
    count2 = string.count('0')
    count3=0
    print(max(count3,min(count1,count2)-1))