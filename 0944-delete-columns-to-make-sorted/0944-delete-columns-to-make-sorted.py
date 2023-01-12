class Solution(object):
    def minDeletionSize(self, strs):
        c = 0
        for itr in range(len(strs[0])):
            comp = strs[0][itr]
            for i in range(1,len(strs)):
                if comp > strs[i][itr]:
                    print(comp,strs[i][itr])
                    c += 1
                    break
                comp = strs[i][itr]
        return c
            
            
            
        """
        :type strs: List[str]
        :rtype: int
        """
        