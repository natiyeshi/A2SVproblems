class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = tickets[k] * len(tickets) - (len(tickets) - (k + 1))
        value = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                tickets[i] -= value
            else:
                tickets[i] -= value - 1
        
        sum_ = 0
        for i in tickets:
            if i < 0: sum_ += abs(i)
                
        return result - sum_