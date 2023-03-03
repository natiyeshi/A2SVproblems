class Solution:
    def check_day(self,weights,day,curr):
        count = 1
        temp = 0
        for i in range(len(weights)):
            if temp + weights[i] > curr:
                count += 1
                temp = 0
            temp += weights[i]
        return count <= day
        

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if self.check_day(weights,days,mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result