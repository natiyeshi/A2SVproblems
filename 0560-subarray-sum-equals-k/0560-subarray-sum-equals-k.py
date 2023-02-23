class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
        counter = 0
        for i, val in enumerate(preSum):
            if val - k in dic:
                counter += dic[val - k] 
            dic[val] += 1
        return counter
        