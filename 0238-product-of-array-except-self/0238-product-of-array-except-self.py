class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        preSum = []
        dic = Counter(nums)
        if 0 in dic:
            if dic[0] > 1:
                return [0 for i in nums]
            else:
                mul_ = 1
                for i in nums:
                    if i != 0: mul_ *= i
                for i in nums:
                    if i == 0: preSum.append(mul_)
                    else: preSum.append(0)
                return preSum
        mul_ = 1
        for i in nums:
            mul_ *= i
        preSum = [int(mul_ / i) for i in nums]
        return preSum
        