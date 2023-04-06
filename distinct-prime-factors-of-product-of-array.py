class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        ans = set()
        def calc(num):
            nonlocal ans
            d = 2
            while d * d <= num:
                while num % d == 0:
                    ans.add(int(d))
                    num /= d
                d += 1 
            if num > 1:ans.add(int(num))
        
        for i in nums:
            calc(i)
        return len(ans)