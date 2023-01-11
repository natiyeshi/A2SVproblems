class Solution(object):
    def queensAttacktheKing(self, queens, king):
        x , y = king
        l = r = t = b = lt = lb = rt = rb = False
        queens = sorted(queens,key = lambda a:abs((king[0] - a[0])**2 + (king[1] - a[1])**2))
        ans = []
        
        for itr in queens:
            if itr[0] == x and itr[1] < y and l == False:
                l = True
                ans.append(itr)
            elif itr[0] == x and itr[1] > y and r == False:
                r = True
                ans.append(itr)
            elif itr[1] == y and itr[0] < x and t == False:
                t = True
                ans.append(itr)
            elif itr[1] == y and itr[0] > x and b == False:
                b = True
                ans.append(itr)
            elif abs(itr[0] - x) == abs(itr[1] - y) and itr[1] < y and itr[0] < x and lt == False:
                lt = True
                ans.append(itr)
            elif abs(itr[0] - x) == abs(itr[1] - y) and itr[1] > y and itr[0] < x and rt == False:
                rt = True
                ans.append(itr)
            elif abs(itr[0] - x) == abs(itr[1] - y) and itr[1] < y and itr[0] > x and lb == False:
                lb = True
                ans.append(itr)
            elif abs(itr[0] - x) == abs(itr[1] - y) and itr[1] > y and itr[0] > x and rb == False:
                rb = True
                ans.append(itr)
                
        return ans
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        