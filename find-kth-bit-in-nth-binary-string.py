class Solution:
    def getFormulate(self,string):
        oldString = string[:]
        for i in range(len(string)):
            if string[i] == "0":
                string[i] = "1"
            else:
                string[i] = "0"
        string.reverse()
        return oldString + ["1"] + string

    def findKthBit(self, n: int, k: int,string = "0",start = 0) -> str:
        if start == n:
            return string[k - 1]
        newString = self.getFormulate(list(string))
        newString = "".join(newString)
        return self.findKthBit(n,k,newString,start + 1)