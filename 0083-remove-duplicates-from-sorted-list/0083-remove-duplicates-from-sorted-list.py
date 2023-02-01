# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        h = ListNode(0)
        temp = ListNode(head.val)
        h.next = temp
      
        while head:
            if head.val != temp.val:
                t = ListNode(head.val)
                temp.next = t
                temp = t
     
            head = head.next
            
        return h.next
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        