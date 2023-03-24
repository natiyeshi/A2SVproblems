class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        def backtrack(temp = [],curr = 0):
            nonlocal result
            for i in range(curr,len(arr)):
                if len(arr[i]) == len(set(arr[i])):
                    result = max(result,len(arr[i]))
                curr = arr[i]
                string = "".join(temp)
                if len(set(curr + string)) == len(curr) + len(string):
                    temp.append(curr)
                    result = max(result,len("".join(temp)))
                backtrack(temp[:],i+1)
                if temp:temp.pop()
        backtrack()
        return result