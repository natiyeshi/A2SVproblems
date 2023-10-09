# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return [False,False,None]
            x = x1 = y = y1 =  False
            z = z1 = None
            if node.left:
                x,y,z = dfs(node.left)
                if z != None:
                    return [x,y,z]
            if node.right:
                x1,y1,z1 = dfs(node.right)
                if z1 != None:
                    return [x1,y1,z1]
            x = (x1 or x) or (p.val == node.val)
            y = (y1 or y) or (q.val == node.val)
            if x and y:
                return [True,True,node]
            return [x,y, None]

        return dfs(root)[-1]