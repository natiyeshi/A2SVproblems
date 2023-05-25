class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        cp = arr.copy()
        ind = -1
        for i in range(len(arr) - 1,0,-1):
            if arr[i] < arr[i - 1]:
                ind = i - 1
                break
        if ind != -1:
            temp = None
            for i in range(ind + 1,len(arr)):
                if arr[i] < arr[ind]:
                    if temp and arr[temp] < arr[i]:
                        temp = i
                    elif temp is None:
                        temp = i
            if temp:
                arr[temp],arr[ind] = arr[ind],arr[temp]
        return arr