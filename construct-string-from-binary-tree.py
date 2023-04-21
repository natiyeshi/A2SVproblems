# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        arr = []
        def dfs(root):
            if root:
                arr.append(str(root.val))
                arr.append("(")
                dfs(root.left)
                arr.append(")")
                arr.append("(")
                dfs(root.right)
                arr.append(")|")
                if arr[-1] == arr[-3] == ")" and arr[-2] == arr[-4] == "(":
                    arr.pop()
                    arr.pop()
                    arr.pop()
                    arr.pop()
                elif arr[-1] == ")" and arr[-2] == "(" and arr[-4].isdigit():
                    arr.pop()
                    arr.pop()
                    
                    
        dfs(root)
        if len(arr) > 2 and arr[-2] == "(" and arr[-1] == ")":
            arr.pop()
            arr.pop()
        return "".join(arr)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: Optional[TreeNode]) -> str:
        if not t:
            return ""
        result = str(t.val)
        if t.left:
            result += "(" + self.tree2str(t.left) + ")"
            if t.right:
                result += "(" + self.tree2str(t.right) + ")"
        elif t.right:
            result += "()(" + self.tree2str(t.right) + ")"
        return result