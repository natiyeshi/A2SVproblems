class Solution(object):
    def threeSum(self, nums):
        ans = []
        
        nums.sort()
        
        for index,target in enumerate(nums):
            # print(index)
            left = index + 1
            right = len(nums) - 1
            
            while left < right :
                
                if target + nums[left] + nums[right] == 0:
                    found = [target,nums[left],nums[right]]
                    if found not in ans:
                        ans.append(found)
                    right -= 1
                    left += 1
                elif target + nums[left] + nums[right] < 0:
                    left += 1
                    
                else:
                    right -=1
                    
        return ans
            
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        