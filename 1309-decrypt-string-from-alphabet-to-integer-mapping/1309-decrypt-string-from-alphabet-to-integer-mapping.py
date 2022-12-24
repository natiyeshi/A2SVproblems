class Solution(object):
    def freqAlphabets(self, s):
            hashs = {}
            a = "a"
            for i in range(1,27):
                if i < 10:
                    hashs[str(i)] = chr(ord(a) + i - 1)
                else:
                    hashs[str(i)+"#"] = chr(ord(a) + i - 1) 
            counter = len(s) - 1
            sen = ""
            
            while counter >= 0:
                if s[counter] == "#":
                    arg = s[counter - 2] +s[counter - 1] +s[counter]
                    sen = hashs[arg] + sen
                    counter -= 3
                else:
                    arg = s[counter]
                    sen = hashs[arg] + sen
                    counter -= 1

            return sen
    

        