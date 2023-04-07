class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp = edges[0]
        if temp[0] in edges[1]:
            return temp[0]
        return temp[1]