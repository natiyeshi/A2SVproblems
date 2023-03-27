class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = []
        m = len(nums)
        nums = set(nums)
        for i in range(1,m + 1):
            if i not in nums:
                temp.append(i)
        return temp