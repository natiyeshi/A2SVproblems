# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        temp = head
        arr = []
        c = 0
        while temp:
            arr.append(temp.val)
            temp = temp.next
        ans = [0 for i in range(len(arr))]
        stack = []
        for i,val in enumerate(arr):
            while stack and arr[stack[-1]] < val:
                ans[stack.pop()] = val
            stack.append(i)
        
        return ans
            
        
        """
        :type head: ListNode
        :rtype: List[int]
        """
        