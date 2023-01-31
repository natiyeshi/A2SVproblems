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
        tp = count
        while tp != right:
            arr.append(temp.val)
            temp = temp.next
            tp += 1
            
        arr.append(temp.val)
        arr.reverse()
        for i in arr:
            start.val = i
            start = start.next
        return head
        
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        