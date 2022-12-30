from collections import Counter

class Solution(object):
    def findWinners(self, matches):
        win = defaultdict(int)
        lose = defaultdict(int)
        
        for x, y in matches:
            win[x] += 1
            lose[y] += 1
        
        res = [[] for _ in range(2)]
        
        for k, v in win.items():
            if lose[k] == 0:
                res[0].append(k)
        
        for k, v in lose.items():
            if v == 1:
                res[1].append(k)
        
        res[0].sort()
        res[1].sort()
        
        return res


          
            
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        