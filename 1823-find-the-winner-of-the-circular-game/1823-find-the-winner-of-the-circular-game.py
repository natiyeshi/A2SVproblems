class Solution(object):
    def findTheWinner(self, n, k):
        friends=[i for i in range(1,n+1)]
        i=0     
        while len(friends)>1:            
            i=(i+k-1)%len(friends)  
            del friends[i]
         
        return friends[0]
        
            
            
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        