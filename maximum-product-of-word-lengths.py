class Solution:
    def maxProduct(self, words: List[str]) -> int:

        temp = []
        for i in words:
            a = 0
            for j in i:
                a |= (1 << (ord(j) - 67)) 
            temp.append(a)
        m = 0
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i] & temp[j] == 0:
                    m = max(m,len(words[i]) * len(words[j]))
        return m