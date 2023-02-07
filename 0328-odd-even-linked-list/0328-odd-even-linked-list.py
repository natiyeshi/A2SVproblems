# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        dummy = ListNode()
        temp = dummy
        
        itr = head
        
        dummy2 = ListNode()
        temp2 = dummy2
        
        c = 0
        
        while itr:
            if c % 2 == 0:
                temp.next = ListNode(itr.val)
                temp = temp.next
            else:
                temp2.next = ListNode(itr.val)
                temp2 = temp2.next
            itr = itr.next
            c += 1
        temp.next = dummy2.next
        
        return dummy.next
        