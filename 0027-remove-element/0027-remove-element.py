class Solution(object):
    def removeElement(self, nums, val):
            c , itr = 0 , 0
            l = len(nums)
            while itr < len(nums):
                if nums[itr] == val:
                    nums.remove(nums[itr])
                    c += 1
                else:
                    itr += 1
            for i in range(c):
                nums.append("_")
            return l - c


        
                
                
        
        
     
        