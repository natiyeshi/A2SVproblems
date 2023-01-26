class Solution(object):
    def maxOperations(self, arr, k):
        arr.sort()
        sm = 0
        lar = len(arr) - 1
        c = 0
        while sm < lar :
            if arr[sm] + arr[lar] == k :
                c += 1
                sm += 1 
                lar -= 1
                
            elif arr[sm] + arr[lar] < k:
                sm += 1
            else:
                lar -= 1
        return c
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        