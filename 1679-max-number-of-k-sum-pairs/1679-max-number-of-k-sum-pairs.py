class Solution(object):
    def maxOperations(self, arr, k):
        arr.sort()
        sm = 0
        lar = len(arr) - 1
        c = set()
        print(arr)
        while sm != lar and sm < len(arr) and lar >= 0 :
            if arr[sm] + arr[lar] == k :
                if (lar,sm) not in c:
                    c.add((sm,lar))
                else:
                    break
                sm += 1 
                lar -= 1
                
            elif arr[sm] + arr[lar] < k:
                sm += 1
            else:
                lar -= 1
        return len(c) 
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        