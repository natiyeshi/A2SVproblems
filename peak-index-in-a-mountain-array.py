class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ind = 1
        while ind in range(len(arr) - 1):
            if arr[ind - 1] < arr[ind] > arr[ind + 1]:
                return ind
            ind += 1
        return -1