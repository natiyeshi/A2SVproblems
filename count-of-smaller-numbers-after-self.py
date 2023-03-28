class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def concure(arr1,arr2):
            nonlocal counter
            arr = []
            l = r = 0
            temp = 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l][0] <= arr2[r][0]:
                    arr.append(arr1[l])
                    counter[arr1[l][1]] += temp
                    l += 1
                else:
                    arr.append(arr2[r])
                    r += 1
                    temp += 1
            while l < len(arr1):
                counter[arr1[l][1]] += temp
                arr.append(arr1[l])
                l += 1
            while r < len(arr2):
                arr.append(arr2[r])
                r += 1
            return arr            
            
        def mergeSort(arr):
            if len(arr) < 2:
                return arr
            m = len(arr) // 2
            left = mergeSort(arr[:m])
            right = mergeSort(arr[m:])
            return concure(left,right)
        counter = {}
        for i in range(len(nums)): counter[i] = 0
        arr = []
        for i,val in enumerate(nums):
            arr.append((val,i))
        mergeSort(arr)
        return list(counter.values())