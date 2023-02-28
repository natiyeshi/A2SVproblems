# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2, arr = None, dummy = None ) -> Optional[ListNode]:
        if arr is None:
            arr = ListNode()
            dummy = arr
        if list1 and list2:
            if list1.val > list2.val:
                temp = ListNode(list2.val)
                arr.next = temp
                arr = arr.next
                return self.mergeTwoLists(list1,list2.next,arr,dummy)
            temp = ListNode(list1.val)
            arr.next = temp
            arr = arr.next
            return self.mergeTwoLists(list1.next,list2,arr,dummy)
        else:
            while list1:
                temp = ListNode(list1.val)
                arr.next = temp
                arr = arr.next
                list1 = list1.next
            while list2:
                temp = ListNode(list2.val)
                arr.next = temp
                arr = arr.next
                list2 = list2.next
            return dummy.next
        
        