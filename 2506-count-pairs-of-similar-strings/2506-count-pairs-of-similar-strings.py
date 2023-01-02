from collections import Counter
class Solution(object):
    def similarPairs(self, words):
        a = 0
        for it,itr in enumerate(words):
            d = Counter(itr)
            alpha1 = d.keys()    
            for j in range(it + 1,len(words)):
                c = True
                d = Counter(words[j])
                alpha2 = d.keys()    
                if len(alpha1) != len(alpha2):
                    c = False
                for i in alpha1:
                    if i not in alpha2:
                        c = False
                if c == True:
                    print(alpha1,alpha2,it)
                    a += 1
        return a



        
        """
        :type words: List[str]
        :rtype: int
        """