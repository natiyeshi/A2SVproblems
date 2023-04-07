from collections import defaultdict
nofv = int(input())
p = int(input())
dic = defaultdict(list)
for i in range(p):
    temp = input().split()
    a = int(temp[0])
    if a == 1:
        dic[temp[1]].append(temp[2])
        dic[temp[2]].append(temp[1])
    else:
        print(*dic[temp[1]])
