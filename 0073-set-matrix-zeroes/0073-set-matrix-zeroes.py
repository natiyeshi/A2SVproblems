class Solution(object):
    def setZeroes(self, matrix):
        arr = []
        r , c = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    arr.append([i,j])
        for itr in arr:
            tempr , tempc = itr
            while tempr < r:
                matrix[tempr][tempc] = 0
                tempr += 1
            tempr , tempc = itr
            while tempc < c:
                matrix[tempr][tempc] = 0
                tempc += 1
            tempr , tempc = itr
            while tempr > -1:
                matrix[tempr][tempc] = 0
                tempr -= 1
            tempr , tempc = itr
            while tempc > -1:
                matrix[tempr][tempc] = 0
                tempc -= 1
        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        