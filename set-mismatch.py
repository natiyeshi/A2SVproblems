class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        temp = Counter(nums)
        for i in temp:
            if temp[i] == 2:
                result.append(i)
        temp = set(nums)
        for i in range(1,len(nums) + 1):
            if i not in temp:
                result.append(i)
        return result