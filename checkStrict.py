# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = list(map(int,input().split(" ")))
num = int(input())
b = True
for _ in range(num):
    ar = list(map(int,input().split(" ")))
    if len(arr) <= len(ar):
        b = False
    for i in ar:
        if i not in arr:
            b = False

if b == False: 
    print(False)
else:
    print(True)
