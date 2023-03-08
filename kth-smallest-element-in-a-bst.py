# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        f = False
        def traverse(root):
            nonlocal ans,f,k
            if root and not f:
                traverse(root.left)
                if k == 1 and not f:
                    ans = root.val
                    f = True
                    return
                k -= 1
                traverse(root.right)
        traverse(root)
        return ans