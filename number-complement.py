class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        result = 0 
        while num != 0:
            if num & 1 == 0:
                result += (2 ** count)
            num >>= 1 
            count += 1
        return result