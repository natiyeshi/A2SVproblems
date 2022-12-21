# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
arr = input()

arr = arr.split(" ")
files = {}

for ar in arr:
    if ar not in files:
        files[ar] = 1
    else:
        files[ar] += 1

for i in files:
    if files[i] == 1:
        print(i)
        break
