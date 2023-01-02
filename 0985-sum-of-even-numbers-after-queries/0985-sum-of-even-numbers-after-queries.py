class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        ans = []
        _sum = 0
            
        for i in nums:
                if i % 2 == 0:
                    _sum += i
            
        for itr in queries:
            if nums[itr[1]] % 2 == 0:
                a = nums[itr[1]]
                nums[itr[1]] += itr[0]
                if nums[itr[1]] % 2 == 0:
                    _sum += itr[0]
                else:
                    _sum -= a
            else:
                nums[itr[1]] += itr[0]
                if nums[itr[1]] % 2 == 0:
                    _sum += nums[itr[1]]
            
            ans.append(_sum)
            # print(_sum)
        
        return ans
    
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        