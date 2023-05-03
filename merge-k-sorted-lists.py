# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        arr = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(arr,(lists[i].val,i))
        while arr:
            val,i = heapq.heappop(arr)
            temp.append(val)
            if lists[i] and lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(arr,(lists[i].val,i))
        result = ListNode()
        dummy = result
        while temp:
            val = heapq.heappop(temp)
            result.next = ListNode(val)
            result = result.next
        return dummy.next