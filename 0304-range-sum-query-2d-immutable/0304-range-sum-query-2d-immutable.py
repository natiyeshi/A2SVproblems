class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                sum_ = matrix[i][j]
                if i - 1 >= 0:
                    sum_ += self.matrix[i - 1][j]
                if j - 1 >= 0:
                    sum_ += self.matrix[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    sum_ -= self.matrix[i - 1][j - 1]
                self.matrix[i][j] = sum_
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = self.matrix[row2][col2]
        if row1 - 1 >= 0:
            sum_ -= self.matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            sum_ -= self.matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            sum_ += self.matrix[row1 - 1][col1 - 1]
        return sum_
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)