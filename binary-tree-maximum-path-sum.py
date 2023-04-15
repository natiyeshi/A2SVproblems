# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")
        def traverse(root):
            nonlocal result
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            m = max(left,right)
            if left == 0 and right != 0:
                result = max(right,root.val + right,result,root.val)
            elif left != 0 and right == 0:
                result = max(left,left + root.val,result,root.val)
            elif left == 0 and right == 0: 
                result = max(result,root.val)
            else:
                result = max(m + root.val,left,right,left + root.val + right,result,root.val)
            r = max(left,right) + root.val

            return max(r,root.val)
        traverse(root)
        return result