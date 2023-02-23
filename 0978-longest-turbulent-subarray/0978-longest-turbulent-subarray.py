class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 3:
            if len(arr) == 1: return 1
            if arr[0] == arr[1]: return 1
            return 2
        st = 0
        while st < len(arr) - 1 and arr[st] == arr[st + 1]:
            st += 1
        
        if st + 1 >= len(arr):
            return 1 
        
        temp = [arr[st],arr[st+1]]
        print(temp,st+1)
        max_ = 2
        right = st + 2
        while right < len(arr):
            if len(temp) < 2:
                temp.append(arr[right])
                right += 1
                continue
            flag = temp[-1] > temp[-2]
            if flag:
                if arr[right] == temp[-1]:
                    temp = [arr[right]]
                elif arr[right] < temp[-1]:
                    temp.append(arr[right])
                else:
                    temp = [temp[-1],arr[right]]
            else:
                if arr[right] == temp[-1]:
                    temp = [arr[right]]
                elif arr[right] > temp[-1]:
                    temp.append(arr[right])
                else:
                    temp = [temp[-1],arr[right]]
                
            right += 1
            max_ = max(len(temp),max_)
            
        return max_