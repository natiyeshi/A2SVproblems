# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        start = 0
        end = len(arr) - 1
        
        while start < end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True
        
        """
        :type head: ListNode
        :rtype: bool
        """
        