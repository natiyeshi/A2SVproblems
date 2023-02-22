class Solution(object):
    def subarraySum(self, nums, k):
        pre = [0]
        sums = defaultdict(int)
        counter = 0
        for i in nums:
            pre.append(pre[-1] + i)
        for ele in pre:
            if ele - k in sums:
                counter += sums[ele - k]
            sums[ele] += 1 
            
        return counter
        
                                                                                                                
        
         
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        