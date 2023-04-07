num = int(input())
result = 0
for i in range(num):
    row = list(map(int,input().split()))
    for j in range(i,num):
        if row[j] == 1:
            result += 1
print(result)
