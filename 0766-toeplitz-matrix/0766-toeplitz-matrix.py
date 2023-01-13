class Solution(object):
    def isToeplitzMatrix(self, matrix):
        
        dic = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j - i in dic:
                    if dic[j - i] != matrix[i][j]:
                        return False
                else:
                    dic[j - i] = matrix[i][j]
        return True
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        