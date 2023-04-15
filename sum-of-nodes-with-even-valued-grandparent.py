# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        def dfs(root,par = False,eat = False):
            nonlocal result
            if root:
                print(root.val,par,eat)
                if eat: 
                    result += root.val
                dfs(root.left,root.val % 2 == 0,par)
                dfs(root.right,root.val % 2 == 0,par)
        dfs(root)
        return result