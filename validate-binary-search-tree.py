# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print("inkkk")
        def dfs(root,m,mi):
            if not root:
                return True
            val = True
            if root.left:
                if root.val <= root.left.val or root.left.val <= mi:
                    return False
                val = val and dfs(root.left,root.val,mi)
            if root.right:
                if root.val >= root.right.val or root.right.val >= m:
                    return False
                val = val and dfs(root.right,m,root.val)
            
            return val
        return dfs(root,float("inf"),float("-inf"))