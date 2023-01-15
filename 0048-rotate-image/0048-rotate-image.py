class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        length = len(matrix)
        i = j = 0
        for c in range(len(matrix)):
            i = j = c - 1
            
            for count in range(1,i+2):
                matrix[i - count][j] , matrix[i][j - count] = matrix[i][j - count] , matrix[i - count][j]       

        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        