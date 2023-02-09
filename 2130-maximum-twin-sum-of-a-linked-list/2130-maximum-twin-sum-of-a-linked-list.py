# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        temp = head
        check = head
        while temp and temp.next:
            temp = temp.next.next
            check = check.next
       
        rev = None

        while check:
            nexts = check.next
            check.next = rev
            rev = check
            check = nexts
        
        _max = 0
        
        while rev:
            _max = max(_max,sum((rev.val,head.val)))
            head = head.next
            rev = rev.next
        return _max
        