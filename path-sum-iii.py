# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        dic = defaultdict(int)
        dic[0] = 1 
        result = 0
        def traverse(root,sum_):
            nonlocal result
            if root:
                sum_ += root.val
                if sum_ - targetSum in dic:
                    result += dic[sum_ - targetSum]
                if sum_ in dic:
                    dic[sum_] += 1
                else:
                    dic[sum_] += 1
                traverse(root.left,sum_)
                traverse(root.right,sum_)
                dic[sum_] -= 1
        traverse(root,0)
        return result