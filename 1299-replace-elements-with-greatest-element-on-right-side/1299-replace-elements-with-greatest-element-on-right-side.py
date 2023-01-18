class Solution(object):
    def replaceElements(self, arr):
        
        maxi=-1
        for index in range(len(arr)-1,-1,-1):
            temp=arr[index]
            arr[index]=maxi        
            maxi=max(maxi,temp)
        return arr
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        