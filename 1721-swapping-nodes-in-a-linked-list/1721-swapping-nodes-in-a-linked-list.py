# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        end = start = head
        
        for _ in range(k - 1):
            end = end.next
        first = end
        while end.next:
            end = end.next
            start = start.next
            
        first.val , start.val = start.val,first.val
        return head
        
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        