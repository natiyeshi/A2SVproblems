# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode()
        temp = dummy
        
        if head is None or head.next is None:
            return head
        
        itr = head
        
        while itr:
            copy = temp
            while copy.next and itr.val > copy.next.val:
                copy = copy.next
            
            if copy and copy.next:
                t = copy.next
                copy.next = ListNode(itr.val)
                copy.next.next = t
            else:
                copy.next = ListNode(itr.val)
            
            itr = itr.next
        
        return dummy.next
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        