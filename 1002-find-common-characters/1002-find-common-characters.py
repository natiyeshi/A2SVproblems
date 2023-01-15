class Solution(object):
    def commonChars(self, words):  
        ans = []
        
        for s in words[0]:
            itr = 1
            find = False
            while itr < len(words):
                if s not in words[itr]:
                    find = False
                    break
                else:
                    find = True
                itr += 1
            i = 1
            if find == True:
                while i < len(words):
                    temp = words[i]
                    temp = list(temp)      
                    temp.remove(s) 
                    words[i] = "".join(temp)
                    i += 1
                ans.append(s)
        return ans