# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def divide(node):
            # if not node:
            #     return [node,node]
            slow = fast = node
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            print(pre.val)
            pre.next = None
            return [node,slow]
        
        def concure(node):
            if not node or not node.next:
                return node
            left,right = divide(node)
            left = concure(left)
            right = concure(right)
            dummy = temp = ListNode()
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            if left:
                temp.next = left
            else:
                temp.next = right
            return dummy.next
        return concure(head)