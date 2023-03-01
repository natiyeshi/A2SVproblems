class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(arr)):
            if stack and arr[stack[-1]] > arr[i]:
                ind = stack[-1]
                while stack and arr[stack[-1]] > arr[i]:
                    curr = stack.pop()
                    if stack:
                        ans += (curr - stack[-1]) * arr[curr] * (ind - curr + 1)
                    else:
                        ans += (curr + 1) * arr[curr] * (ind - curr + 1)
            stack.append(i)
        
        ind = stack[-1]
        while stack:
            curr = stack.pop()
            if stack:
                ans += (curr - stack[-1]) * arr[curr] * (ind - curr + 1)
            else:
                ans += (curr + 1) * arr[curr] * (ind - curr + 1)

        return ans % (10**9 + 7)