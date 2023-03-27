# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        dummy = root
        stack = [root]
        for i in preorder[1:]:
            currNode = TreeNode(i)
            if stack and stack[-1].val > currNode.val:
                stack[-1].left = currNode
                stack.append(currNode)
                continue
            temp = None
            while stack and stack[-1].val < currNode.val:
                temp = stack.pop()
            temp.right = currNode
            stack.append(currNode)
        return dummy