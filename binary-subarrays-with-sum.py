class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
        count = Counter(pre)
        result = 0
        pre = list(set(pre[1:]))
        if goal == 0:
            temp = 0
            for i in nums:
                if i == 0:
                    temp += 1
                else:
                    result += (temp * (temp + 1)) / 2 
                    temp = 0
            
            result += (temp *(temp + 1)) / 2
            return int(result)
        for i in pre:
            if i - goal in count:
                result += count[i - goal] * count[i]
        return result