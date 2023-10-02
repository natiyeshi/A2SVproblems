class Node:
    def __init__(self,val):
        self.par = None
        self.val = None
        self.next = None
        self.count = 0 

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
           stack.append((i,1))
           if len(stack) > 1 and stack[-1][0] == stack[-2][0]: 
               stack[-1] = (i,stack[-2][1] + 1)
           if len(stack) >= k and stack[-1][1] == k:
                for j in range(k):
                    stack.pop()
        result = [i[0] for i in stack]
        return ''.join(result)