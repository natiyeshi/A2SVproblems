class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p , i = 0 , 0
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        
        # while p < n:
        #     if nums1[i] > nums2[p] or (nums1[i] == 0 and i >= m - n):
        #         nums1.insert(i,nums2[p])
        #         nums1.pop()
        #         p += 1
        #     i += 1
            
            
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        