class Solution(object):
    def addSpaces(self, s, spaces):
      
        string = []
        itr = p = 0 
        while itr < len(s):
            if p < len(spaces) and itr == spaces[p]:
                p += 1
                string.append(" ")
            else:
                # print(itr)
                string.append(s[itr])
                itr += 1
        return "".join(string)
        