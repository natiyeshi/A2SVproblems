def maximum(nums,i):
    flag = nums[i] > 0
    j = i
    if flag:
        while j < len(nums):
            if nums[j] >= 0:
                j += 1
            else:
                break
    else:
        while j < len(nums):
            if nums[j] <= 0:
                j += 1
            else:
                break
    return [max(nums[i:j]), j]
            

num = int(input())


for _ in range(num):
    n = int(input())
    nums = list(map(int,input().split()))
    i = 0
    m = 0
    while i < n:
        rtr = maximum(nums,i)
        m += rtr[0]
        i = rtr[1]
    print(m)
    
    
    
    
    
        
        
        
    
        
    
