class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            arr = board[i]
            temp1 = []
            for j in range(9):
                if board[i][j] != ".":
                    temp1.append(board[i][j])
            temp2 = set(temp1)
            if len(temp1) > len(temp2):
                return False
        trans = list(map(list, zip(*board)))
        for i in range(9):
            arr = trans[i]
            temp1 = []
            for j in range(9):
                if trans[i][j] != ".":
                    temp1.append(trans[i][j])
            temp2 = set(temp1)
            if len(temp1) > len(temp2):
                return False
        indexs = [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]
        for itr in indexs:
            a , b = itr
            a -= 1
            b -= 1
            temp = []
            for i in range(itr[0] - 1,itr[0]+2):
                for j in range(itr[1] - 1,itr[1]+2):
                    if board[i][j] != ".":
                        temp.append(board[i][j])
               
            temp2 = set(temp)
            if len(temp) > len(temp2):
                print(temp,temp2)
                return False
            
        return True
        
                
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        