# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        temp = head
        for i in range(len(arr)-1,-1,-1):
            temp.val = arr[i]
            temp = temp.next
            
        return head
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        