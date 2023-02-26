class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rsum = 0
        counter = 0
        ch = defaultdict(int)
        ch[0] = 1
        for i in nums:
            rsum += i
            key = rsum % k
            if key in ch:
                counter += ch[key]
            ch[key] += 1
                
        return counter
        