# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insert(arr=[]):
            if not arr:
                return 
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = insert(arr[:mid])
            root.right = insert(arr[mid+1:])
            return root
            
        return insert(nums)