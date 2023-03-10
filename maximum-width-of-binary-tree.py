# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        def traverse(root,level = 0,temp = 1):
            if not root:
                return 
            dic[level].append(temp)
            traverse(root.left,level + 1,temp * 2)
            traverse(root.right,level + 1,temp * 2 + 1)
        traverse(root)
        result = 1
        for itr in dic:
            result =  max(result,dic[itr][-1]-dic[itr][0] + 1)
            print(dic[itr])
        return result