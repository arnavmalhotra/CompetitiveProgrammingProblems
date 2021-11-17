# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(input())

print("This is the number of tests: " +str(tests))

for num in range(0,tests):
    print("This is number: "+str(num))
    SetANums = int(input())
    setA = set(input().split())
    SetBNums = int(input())
    setB = set(input().split())
    print(setB.issubset(setA))