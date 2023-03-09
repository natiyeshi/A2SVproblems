# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = defaultdict(list)

        def traverse(root,col,width):
            if not root:
                return col
            temp[col].append([root.val,width,col])
            traverse(root.left,col - 1,width + 1)
            traverse(root.right,col + 1,width + 1)
        traverse(root,0,0)
        temp = list(dict(sorted(temp.items(),key = lambda k:k[0])).values())
        for i in range(len(temp)):
            t = sorted(temp[i],key = lambda k: (k[1],k[2],k[0]))    
            t2 = []
            for j in t:
                t2.append(j[0])
            temp[i] = t2
        print(temp)
        return temp