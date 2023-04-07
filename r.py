from collections import Counter 

l = int(input())
sink = []
source = [True for i in range(l)]
for i in range(l):
    row = list(map(int,input().split()))
    f = False
    for j in range(l):
        if row[j] == 1:
            f = True
            source[j] = False
    if not f:sink.append(str(i + 1))
source = [str(i + 1) for i in range(len(source)) if source[i]]
print(len(source)," ".join(source))
print(len(sink)," ".join(sink))
