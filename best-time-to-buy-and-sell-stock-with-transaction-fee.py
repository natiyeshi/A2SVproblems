class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        eff = prices[0]
        for i in range(len(prices)):
            profit = max(profit,prices[i] - eff - fee)
            eff = min(eff,prices[i] - profit)
            print(i,profit,eff)
        return profit