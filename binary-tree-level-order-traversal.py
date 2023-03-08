# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        temp = defaultdict(list)
        def traverse(root,key = 1):
            if root:
                traverse(root.left , key + 1)
                traverse(root.right, key + 1)
                temp[key].append(root.val)
        traverse(root)
        temp=dict(sorted(temp.items(), key=lambda item: item[0]))
        return temp.values()