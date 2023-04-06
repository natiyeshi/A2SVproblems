class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
       result = 0

       for i in range(len(nums)):
           last = nums[i]
           for j in range(i,len(nums)):
               last = math.gcd(last,nums[j]) 
               if  last == k: result += 1
       return result