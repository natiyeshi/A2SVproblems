# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        if not head or not head.next:
            return head
    
        fast = head.next
        slow = head
        
        dummy = ListNode(0)
        dummy.next = slow
        
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
            
        slow.next = None
        
        return dummy.next
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        