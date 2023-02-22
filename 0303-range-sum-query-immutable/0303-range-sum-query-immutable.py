class NumArray(object):

    def __init__(self, nums):
        self.arr = nums
        self.pre = [ 0 ]
        for i in nums:
            self.pre.append(self.pre[-1] + i)
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        return self.pre[right + 1] - self.pre[left]
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)