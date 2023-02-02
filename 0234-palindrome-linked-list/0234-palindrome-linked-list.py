# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        fast = head
        slow = head
        
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                temp = slow.next
                slow.next = None
                slow = temp
                break
            if not fast:
                temp = slow.next
                slow.next = None
                slow = temp
                break
            slow = slow.next
            
        rev = None
        while slow:
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp
        
        
        while rev and head:
            if rev.val != head.val:
                return False
            head = head.next
            rev  = rev.next
        return True
        """
        :type head: ListNode
        :rtype: bool
        """
        