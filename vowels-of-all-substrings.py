class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(["a","e","o","i","u"])
        result = 0
        for i,ch in enumerate(word):
            if ch in vowels:
                l = i
                r = len(word) - i - 1
                result += 1 + l + r + (l * r)
        return result