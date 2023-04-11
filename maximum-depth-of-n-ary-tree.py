"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if len(root.children) < 1:
            return 1
        counter = 0
        for r in root.children:
            counter= max(counter,self.maxDepth(r))
        return counter + 1