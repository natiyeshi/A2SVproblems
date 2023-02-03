# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        
        rev = None
        top = head
        while top:
            nexts = top.next
            top.next = rev
            rev = top
            top = nexts
       
        dummy = ListNode(0)
        
        copy = dummy
        copy.next = ListNode(rev.val)
        copy = copy.next
        rev = rev.next
        while rev:
            if copy.val <= rev.val:
                copy.next = ListNode(rev.val)
                copy = copy.next
            rev = rev.next
        
        files = dummy.next
        reverse = None
        while files:
            nexts = files.next
            files.next = reverse
            reverse = files
            files = nexts
        
        return reverse
        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        