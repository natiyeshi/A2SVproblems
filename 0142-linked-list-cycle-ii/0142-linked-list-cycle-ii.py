# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        runner = head
        walker = head
        flag = False
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                flag = True
                break
           
        if not flag:
            return None
        
        while head != walker:
            head = head.next
            walker = walker.next
        return head
                
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        