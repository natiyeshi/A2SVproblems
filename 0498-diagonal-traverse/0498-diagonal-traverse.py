class Solution(object):
    def findDiagonalOrder(self, mat):
        arr = []
        x = y = 0
        arr.append(mat[x][y])
        _max = len(mat)
        _max2 = len(mat[0])
        b = False
        if _max == 1:
            return mat[0]
        if len(mat[0]) == 1:
            for i in range(1,_max):
                arr.append(mat[i][0])
            return arr
        while x != _max2 - 1 or y !=  _max - 1:
            if b == False:
                if x + 1 < _max2:
                    x += 1
                else:
                    y += 1
                while x >= 0 and y < _max:
                    arr.append(mat[y][x])
                    if y + 1 >= _max or x - 1 < 0:
                        break
                    x -= 1
                    y += 1
                        
            else:
                if y + 1 < _max:
                    y += 1
                else:
                    x += 1
                while y >= 0 and x < _max2:
                    arr.append(mat[y][x])
                    if x + 1 >= _max2 or y - 1 < 0:
                        break
                    y -= 1
                    x += 1
            b = not b
                
        return arr
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        