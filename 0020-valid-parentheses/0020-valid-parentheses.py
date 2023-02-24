class Solution:
    def isValid(self, s: str) -> bool:
        bra = []
        match = {"(" : ")","{":"}","[":"]"}
        for i in s:
            if i == "(" or i == "{" or i == "[":
                bra.append(i)
            else:
                if len(bra) < 1 or match[bra.pop()] != i:
                    return False
        return False if len(bra) > 0 else True
        