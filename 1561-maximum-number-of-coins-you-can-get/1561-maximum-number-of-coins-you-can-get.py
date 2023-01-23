class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        s = 0
        while len(piles) != 0:
            piles.pop(0)
            piles.pop()
            s += piles.pop()
        return s;
        
        """
        :type piles: List[int]
        :rtype: int
        """
        