# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        temp = head
        if temp.next == None or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        rev = None
        
        for i in range(right - left + 1):
            nexts = curr.next
            curr.next = rev
            rev = curr
            curr = nexts
        
        prev.next.next = curr
        prev.next = rev      
        
        return dummy.next
        
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        