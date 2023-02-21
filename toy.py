from collections import defaultdict
# ice_cream = defaultdict(lambda: 'Vanilla')

n,m = list(map(int,input().split()))
nums = list(map(int,input().split()))

dics = defaultdict(int)
for _ in range(m):
    dics[input()] += 1

nums.sort()
dics = dict(sorted(dics.items(), key=lambda item: item[1],reverse = True))
c = 0
_min = 0
for i in dics:
    _min += dics[i] * nums[c]
    c += 1

nums.reverse()

_max = 0
c = 0
for i in dics:
    _max += dics[i] * nums[c]
    c += 1
    
print(_min,_max)
