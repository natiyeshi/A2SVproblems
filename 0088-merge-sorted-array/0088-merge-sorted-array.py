class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # for i in range(n):
        #     nums1.pop()
        # nums1.extend(nums2)
        # nums1.sort()
        # [-1,-1,-1,,0,0,0,0,3,0,0,0,0,0,0]
        # [,,,,1,2]
        # 
        i = m - 1      # nums1's index (actual nums)
        j = n - 1      # nums2's index
        k = m + n - 1  # nums1's index (next filled position)

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        
                
        
            
            
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        