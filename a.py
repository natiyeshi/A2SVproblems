length = int(input())
result = []
for j in range(length):
    col = list(map(int,input().split()))
    arr = []
    for i in range(length):
        if col[i] == 1:
            arr.append(str(i+1))

    print(len(arr)," ".join(arr))
