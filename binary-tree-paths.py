# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def traverse(root,string = ""):
            if root:
                string += str(root.val)
                if not root.left and not root.right:
                    result.append(string)
                    string = ""
                else:
                    string += "->"
                traverse(root.left,string)
                traverse(root.right,string)                
        traverse(root)
        return result