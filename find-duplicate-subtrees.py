# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
       
        visited = defaultdict(int)
        result = []
        def dfs(root):
            if not root:
               return ""
            l = dfs(root.left) + "l"
            r = dfs(root.right) + "r"
            ans = (l + r + str(root.val) + ",")
            if  visited[ans] == 0:
                visited[ans] += 1
            elif visited[ans] > 0:
                visited[ans] = -1
                result.append(root)
            return ans
        dfs(root) 
        return result 

"""
{'4,': 3, '4,
2,': 2, '4,
2,4,3,': 1, 
'4,2,4,2,4,3,1,': 1})
"""