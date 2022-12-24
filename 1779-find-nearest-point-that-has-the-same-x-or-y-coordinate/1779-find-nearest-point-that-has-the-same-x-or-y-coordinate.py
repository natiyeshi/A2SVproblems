import math

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        arr = []
        for index, itr in enumerate(points):
            if itr[0] == x or itr[1] == y:
                arr.append(index)
        ind = -1
        small = None
        for itr in arr:
            cal1 = abs(points[itr][0] - x) 
            cal2 = abs(points[itr][1] - y) 
            temp = cal1 + cal2
            if small == None or small > temp:
                small = temp
                ind = itr
        return ind
        
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        