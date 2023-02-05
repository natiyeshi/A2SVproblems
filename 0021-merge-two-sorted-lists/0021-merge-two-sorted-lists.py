# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode(0)
        temp = dummy
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            else:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            temp = temp.next
        
        while list1:
            temp.next = ListNode(list1.val)
            temp = temp.next
            list1 = list1.next
        while list2:
            temp.next = ListNode(list2.val)
            temp = temp.next
            list2 = list2.next
        
        return dummy.next
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        