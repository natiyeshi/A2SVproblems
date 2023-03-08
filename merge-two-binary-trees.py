# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2) -> Optional[TreeNode]:
        
        def merge(tree1,tree2):
            value = 0
            if not tree1 and not tree2:
                return 
            if not tree1:
                return tree2
            if not tree2:
                return tree1
            
            tree1.val += tree2.val
            left = merge(tree1.left,tree2.left)    
            if left:
                tree1.left = left
            right = merge(tree1.right,tree2.right)
            if right:
                tree1.right = right
            return tree1

        return merge(root1,root2)