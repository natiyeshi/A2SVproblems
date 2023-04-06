class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        def backtrack(b = 0,c = 1):
            nonlocal ans
            if int.bit_count(b) == n:
                ans += 1
            for i in range(n):
                if (i + 1) % c != 0 and c % (i + 1) != 0:
                    continue
                if b & (1 << i) == 0:
                    b |= (1 << i)
                    backtrack(b,c + 1)
                    b &= ~(1 << i)
        backtrack()
        return ans