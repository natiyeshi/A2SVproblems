class Solution(object):
    def matrixReshape(self, mat, r, c):
        if r * c != len(mat) * len(mat[0]):
            return mat
        arr = [[0 for _ in range(c)] for _ in range(r)]
        k = z = 0
        for i in range(r):
            for j in range(c):
                arr[i][j] = mat[k][z]
                z += 1
                if z >= len(mat[k]):
                    k += 1
                    z = 0
        return arr    
                
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        