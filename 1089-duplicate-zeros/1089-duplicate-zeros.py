class Solution(object):
    def duplicateZeros(self, arr):
        itr = 0
        while itr < len(arr):
            if arr[itr] == 0:
                arr.insert(itr,0)
                arr.pop()
                itr += 1
            itr += 1
        
            
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        