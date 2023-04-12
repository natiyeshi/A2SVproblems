# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(root,ans = []):
            nonlocal result
            if not root:
               return
            ans.append(str(root.val))
            right = dfs(root.left,ans[:]) 
            left = dfs(root.right,ans[:])
            if not root.left and not root.right:
                result.append(int("".join(ans)))
                return
        dfs(root)
        
        return sum(result)