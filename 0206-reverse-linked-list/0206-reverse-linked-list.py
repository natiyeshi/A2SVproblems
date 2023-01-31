# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        temp = head
        prev = None
        while temp:
            
            nexts = temp.next
            temp.next = prev
            prev = temp
            temp = nexts
            
        return prev
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        