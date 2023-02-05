# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        li1 = l1
        li2 = l2
        re = 0
        dummy = ListNode()
        temp = dummy
        while li1 and li2:
            sums = li1.val + li2.val + re
            if sums > 9: 
                re = int(str(sums)[0])
                temp.next = ListNode(int(str(sums)[1]))
            else:
                re = 0
                temp.next = ListNode(sums)
            
            temp = temp.next
            
            li1 = li1.next          
            li2 = li2.next
        
        while li1:
            sums = li1.val + re
            if sums > 9: 
                re = int(str(sums)[0])
                temp.next = ListNode(int(str(sums)[1]))
            else:
                re = 0
                temp.next = ListNode(sums)
            li1 = li1.next
            temp = temp.next
                        
        while li2:
            sums = li2.val + re
            if sums > 9: 
                re = int(str(sums)[0])
                temp.next = ListNode(int(str(sums)[1]))
            else:
                re = 0
                temp.next = ListNode(sums)
            li2 = li2.next
            temp = temp.next
        if re != 0:
            temp.next = ListNode(re)
            temp = temp.next
            
        return dummy.next
    
    
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        