class Solution(object):
    def printVertically(self, s):
        string = s.split(" ")
        ans = []
        max_ = 0
        for itr in string:
            if len(itr) > max_:
                max_ = len(itr)
        for itr in range(max_):
            a = []
            for i in range(len(string)):
                if itr < len(string[i]):
                    a.append(string[i][itr])
                else:
                    a.append(" ")
            i  = len(a) - 1
            
            while a[i] == " " and i >= 0:
                i -= 1
            a = a[:i+1]
            ans.append("".join(a))

        return ans
        """
        :type s: str
        :rtype: List[str]
        """
        