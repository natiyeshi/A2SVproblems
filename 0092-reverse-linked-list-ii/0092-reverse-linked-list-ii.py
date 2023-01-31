# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        temp = head
        if temp.next == None or left == right:
            return head
        count = 1
        while count != left:
            temp = temp.next
            count += 1
        arr = []
        start = temp
        while count != right:
            arr.append(temp.val)
            temp = temp.next
            count += 1
        arr.append(temp.val)
        
        for i in range(len(arr)-1,-1,-1):
            start.val = arr[i]
            start = start.next
        return head
        
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        