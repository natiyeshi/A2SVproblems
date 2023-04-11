"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        answer = 0
        target = None
        dic = {}
        for itr in employees:
            dic[itr.id] = itr
            if itr.id == id:
                target = itr

        def dfs(employe):
            nonlocal answer
            stack = employe.subordinates
            answer += employe.importance
            for i in stack:
                dfs(dic[i])
        dfs(target)

        return answer