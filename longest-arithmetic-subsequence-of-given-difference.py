class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        run = {}
        for i in arr:
            if i - difference not in run: 
                if i not in run:
                    run[i] = 1
            else:
                run[i] = run[i - difference] + 1
                del run[i - difference]
        result = 1
        if difference == 0:
            run = Counter(arr)
        for i in run:
            result = max(result,run[i])
        

        return result