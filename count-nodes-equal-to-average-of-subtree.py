# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # [sum,number of elements]
        if not root: return 0
        max_ = 0
        def traverse(root):
            nonlocal max_
            if not root:
                return [0,0]
            left = traverse(root.left)
            right = traverse(root.right)
            temp = [left[0] + right[0] + root.val, left[1] + right[1] + 1]
            if temp[1] > 0:
                result = temp[0] // temp[1]
                if result == root.val:
                    print(temp)
                    max_ += 1
            return temp
        traverse(root)
        return max_