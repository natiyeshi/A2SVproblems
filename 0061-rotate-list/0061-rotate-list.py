# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if head == None:
            return head
        if head.next == None:
            return head
        num = 0
        temp = head
        while temp:
            num += 1
            temp = temp.next
        k = k % num
        for i in range(k):
            las = head
            last = None
            while las.next:
                last = las
                las = las.next
            # print(last.val)
            temp = last.next
            temp.next = head
            head = temp
            last.next = None
            
        return head
            
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        