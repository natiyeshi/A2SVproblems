class Solution(object):
    def fib(self, num):
        arr = [0,1]
        sum = 0
        if num == 0: return 0
        if num == 1: return 1
        for i in range(2,30):
            arr.append(arr[i-1] + arr[i-2])
        sum = arr[num - 1] + arr[num - 2]    
        return sum
        
        
