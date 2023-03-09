# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def traverse(root):
            
            if not root:
                return 0
            count[root.val] += 1
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        result = dict(sorted(count.items(),key = lambda k: k[1],reverse=True))
        ans = []
        last = None
        for i in result:
            if not last or result[i] >= last:
                last = result[i]
                ans.append(i)
        
        return ans