class Solution:
    def knightDialer(self, n: int) -> int:
        ways = {
            0 : [6,4],
            1 : [8,6],
            2 : [9,7],
            3 : [4,8],
            4 : [0,9,3],
            5 : [],
            6 : [0,1,7],
            7 : [6,2],
            8 : [1,3],
            9 : [4,2],
        }
        arr = [[1] * 10 for i in range(n)] 
        for i in range(1,n):
            for j in range(10):
                count = 0
                for k in ways[j]:
                    count += arr[i - 1][k] % (10**9 + 7)
                arr[i][j] = count
        return sum(arr[n - 1]) % (10**9 + 7)