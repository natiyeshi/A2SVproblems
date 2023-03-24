class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        count = {i : 0 for i in range(n)}
        result = 0
        def backtrack(temp,c = 0,curr = 0):
            nonlocal result
            
            if list(temp.values()).count(0) == n:  
                result = max(result,c)
            for i in range(curr,len(requests)):
                a , b = requests[i]
                temp[a] -= 1
                temp[b] += 1
                c += 1
                backtrack(temp,c,i + 1)
                c -= 1
                temp[a] += 1
                temp[b] -= 1
        backtrack(count.copy())
        return result