class Solution(object):
    def validMountainArray(self, arr):
        
        inc = True
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                    return False
            if inc == True:
                if arr[i] > arr[i + 1]:
                    if i == 0:
                        return False
                    else:
                        inc = False
            else:
                if arr[i] < arr[i+1]:
                    return False
        if inc == True:
            return False
        return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        