class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        result = float("inf")
        top = sum(grid[0])
        bottom = 0

        for i in range(length):
            top -= grid[0][i]
            result = min(result, max(top, bottom))
            bottom += grid[1][i]

        return result
        # pre = []
        # for itr in grid:
        #     temp = [0]
        #     for j in itr:
        #         temp.append(temp[-1] + j)
        #     pre.append(temp[1:])
        # ans = []
        # print(pre)
        # length = len(grid[0])
        # for i in range(length):
        #     t = 0
        #     temp1 ,temp2= 0,0
        #     if i != length - 1:
        #         temp1 = (pre[0][-1] - pre[0][i]) 
        #     if i > 0:
        #         temp2 = pre[1][i - 1]
                
        #     ans.append([sum((temp1,temp2)),max(temp1,temp2),temp1,temp2])
        # print(ans)
        # ans.sort()
        # return ans[0][1]