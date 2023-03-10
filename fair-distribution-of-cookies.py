class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        result = float("inf") 
        cookies.sort(reverse=True)
        def backtrack(ind,ans):
            nonlocal result
            if ind >= len(cookies):
                result = min(max(ans),result)
                return
            if result <= max(ans):
                return
            for i in range(len(ans)):
                ans[i] += cookies[ind]
                backtrack(ind + 1,ans.copy())
                ans[i] -= cookies[ind]

        temp = [0] * k
        backtrack(0,temp)
        return result