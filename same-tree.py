# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        checker = True
        def check(p,q):
            nonlocal checker
            if (q and not p) or (not q and p):
                checker = False
            elif q and p:
                check(p.left,q.left)
                if q.val != p.val:
                    checker = False
                check(p.right,q.right)
        check(p,q)
        return checker