# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = float("-inf")
        b = True
        def traverse(root):
            nonlocal arr , b
            if root:
                traverse(root.left)
                if root.val > arr:
                    arr = root.val
                else:
                    b = False       
                traverse(root.right)
        traverse(root)
        return b