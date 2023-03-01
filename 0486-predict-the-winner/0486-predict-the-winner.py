class Solution:
    def PredictTheWinner(self, nums,left = 0, right = 1,curr = True) -> bool:
        if len(nums) < 3:
            return True
        if (len(nums) - right + 1) - left == 1:
            ind = 0
            values = [0, 0]
            if not curr: ind = 1 
            values[ind] += nums[left]
            return values
        
        if curr:
            ans1 = self.PredictTheWinner(nums,left + 1,right,not curr)
            ans1[0] += nums[left]
            
            ans2 = self.PredictTheWinner(nums,left,right+1,not curr)
            ans2[0] += nums[len(nums) - right]
            if ans1[0] >= ans2[0]:
                if  left == 0 and right == 1:
                    print(ans1)
                    return ans1[0] >= ans1[1]
                return ans1
            else:
                if  left == 0 and right == 1:
                    print(ans2)
                    return ans2[0] >= ans2[1]
                return ans2
        else:
            ans1 = self.PredictTheWinner(nums,left + 1,right,not curr)
            ans1[1] += nums[left] 
            
            ans2 = self.PredictTheWinner(nums,left,right+1,not curr)
            ans2[1] += nums[len(nums) - right] 
            if ans1[1] >= ans2[1]:
                if left == 0 and right == 1:
                    return ans1[0] >= ans1[1]
                return ans1
            else:
                if left == 0 and right == 1:
                    return ans2[0] >= ans2[1]
                return ans2
            