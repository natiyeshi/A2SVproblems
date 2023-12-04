class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = []
        for i in logs:
            arr.append((i[0],1))
            arr.append((i[1],-1))
        arr.sort()
        d = defaultdict(int)
        count = 0
        for val,ty in arr:
            if ty == 1:
                count += 1
                d[val]= count
            else:
                count -= 1
                d[val] = count
        result = 0
        ans = 0
        for i in d:
            if d[i] > result:
                ans = i
                result = d[i]
        return ans
               
        
