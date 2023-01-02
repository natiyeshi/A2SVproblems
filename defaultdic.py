# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n , m = list(map(int,input().split(" ")))
ans = []
narr = defaultdict(list)
# print(n)
for c in range(n):
    narr[str(input())].append(c + 1)
    # print(c)
# print("hiii")
for _ in range(m):
    char = input()
    s = ""
    if char in narr:
        print(" ".join(map(str,narr[char])))
    else:
        print("-1")
    
