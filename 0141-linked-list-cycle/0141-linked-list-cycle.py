# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        if head is None:
            return False
        runner = head
        walker = head
        
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                return True
            
        return False
        
        
        """
        :type head: ListNode
        :rtype: bool
        """
        