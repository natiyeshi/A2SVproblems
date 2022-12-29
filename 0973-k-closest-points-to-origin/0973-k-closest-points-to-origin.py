class Solution(object):
    def kClosest(self, points, k):
    
        ans = []
        min_ = []
        
        points = sorted(points, key = lambda val: val[0] **2 +val[1]**2)
        return points[:k]
          
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        