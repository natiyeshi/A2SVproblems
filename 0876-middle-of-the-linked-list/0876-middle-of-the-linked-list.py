# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        mid = head
        end = head
        
        while end and end.next:
            end = end.next.next
            mid = mid.next
        return mid
        
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        