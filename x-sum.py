
from collections import defaultdict
def re(arr):
    mdia = defaultdict(int)
    adia = defaultdict(int)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            mdia[j - i] += arr[i][j]
            adia[j + i] += arr[i][j]
    max_ = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if mdia[j - i] + adia[j + i]  - arr[i][j] > max_:
                max_ = mdia[j - i] + adia[j + i] - arr[i][j]
    print(max_)
num = int(input())
for _ in range(num):
    r,c = list(map(int,input().split()))

    arr = [[0 * c] for _ in range(r)]
    for i in range(r):
        arr[i] = list(map(int,input().split()))
    re(arr)
