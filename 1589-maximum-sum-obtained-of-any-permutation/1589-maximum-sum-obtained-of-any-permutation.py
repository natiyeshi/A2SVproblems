class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        rep = [0 for i in nums]
        nums.sort()
        
        for start , end in requests:
            rep[start] += 1
            if end + 1 < len(nums):
                rep[end + 1] -= 1
        
        preSum = [0]
        for i in rep:
            preSum.append(preSum[-1] + i)
        preSum = preSum[1:]
        
        dic = []
        for i in range(len(preSum)):
            dic.append((preSum[i],i))
        
        dic = sorted(dic)
        c = 0
        for item in dic:
            rep[item[1]] = nums[c]
            c += 1
            
        sum_ = 0
        lastPre = [0]
        for i in rep:
            lastPre.append(lastPre[-1] + i)
        lastPre = lastPre[1:]
        
        for start, end in requests:
            sum_ += lastPre[end]
            if start - 1 > -1:
                sum_ -= lastPre[start - 1]
        return sum_ % ( 10 ** 9 + 7 )
    