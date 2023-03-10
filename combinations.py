class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(start,temp = []):
            
            if len(temp) == k:
                answer.append(temp)
                return
            for i in range(start + 1,n+1):
                backtrack(i,temp + [i])

            
        for i in range(1 , n - k + 2):
            backtrack(i,[i])
        
        return answer