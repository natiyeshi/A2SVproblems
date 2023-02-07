#https://codeforces.com/problemset/problem/1174/B
size = int(input())
lis = list(map(int, input().split()))
even =odd=False
for num in lis:
    if num%2 == 0:
        even = True
    else:
        odd =True
if even and odd:
    lis.sort()
    print(*lis)
else:
    print(*lis)
