# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        temp = head
        arr = []
        while temp:
            if temp.val < x:
                arr.append(temp.val)  
                temp.val = -222
            temp = temp.next
        if not arr:
            return head
        first = last = ListNode(-222)
        t1 = t2 = None
        for i in range(len(arr)):
            t1 = ListNode(arr[i])
            last.next = t1
            last = last.next
         
        curr = last
        while head:
            if head.val != -222:
                curr.next = head
                curr = head    
            head = head.next
        curr.next = None
        return first.next
            
        
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        