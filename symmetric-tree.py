# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(temp1,temp2):
            if not temp1 and not temp2:
                return True
            if (temp1 and not temp2) or (temp2 and not temp1):
                return False
            if temp1.val != temp2.val:
                return False
            b1 = check(temp1.left,temp2.right)
            b2 = check(temp1.right,temp2.left)
            return b1 and b2
        return check(root.left,root.right)