class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        while tickets[k] != 0:
            for j in range(len(tickets)):
                if tickets[j] != 0:
                    tickets[j] -= 1
                    result += 1
                if tickets[k] == 0: return result
        return result