class Solution(object):
    def moveZeroes(self, arr):
        
        curr = 0
        zero = 0
        
        
        for i in range(len(arr)):
            if arr[zero] == 0:
                zero += 1
            else:
                arr[zero], arr[curr] = arr[curr],arr[zero]
                zero += 1
                curr += 1
        return arr