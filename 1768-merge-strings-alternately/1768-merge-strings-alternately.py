class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        if len(word2) < len(word1):
            small = len(word2)
            lar = len(word1)
        else :
            lar = len(word2)
            small = len(word1)
            
            
        string = ""
        for i in range(small):
            string += word1[i] + word2[i]
        for i in range(small,lar):
            if len(word1) > len(word2):
                string += word1[i]
            else:
                string += word2[i]
                
        return string
    
    
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        