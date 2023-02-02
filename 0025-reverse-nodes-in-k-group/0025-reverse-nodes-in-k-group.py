# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        copy = head
        n = 0
        while copy:
            copy = copy.next
            n += 1
        
        revStart = head
        revNext = head
        dummy = None
        
        for _ in range(n // k):
            
            for _ in range(k - 1):
                revNext = revNext.next
            revNext = revNext.next
            
            rev = None
            while revStart != revNext:
                nexts = revStart.next
                revStart.next = rev
                rev = revStart
                revStart = nexts
            
            if dummy is None:
                dummy = rev
            else:
                temp = dummy
                while temp.next:
                    temp = temp.next
                temp.next = rev
            
            revStart = revNext
        
        temp = dummy
        while temp.next:
            temp = temp.next
    
        temp.next = revNext
        return dummy        
            
        
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        