class Solution(object):
    def intersection(self, nums1, nums2):
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
        return ans
                  
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        