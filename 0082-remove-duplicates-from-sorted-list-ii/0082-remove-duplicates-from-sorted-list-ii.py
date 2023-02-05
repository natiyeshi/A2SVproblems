# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        temp = head
        if temp is None or temp.next is None:
            return head
        newNode = ListNode(temp.val)
        ret = newNode
        arr = set()
        temp = temp.next
        while temp:
            if newNode.val == temp.val:
                arr.add(temp.val)
            else:
                newNode.next = ListNode(temp.val)
                newNode = newNode.next
            temp = temp.next
        
        newNode = ret
        copy = ListNode(0)
        last = copy
        while newNode:
            if newNode.val not in arr:
                last.next = ListNode(newNode.val)
                last = last.next
            newNode = newNode.next
            
        return copy.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
        