class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.end = False

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        head = TrieNode()
        for word in words:
            temp = head
            for i in word:
                if i not in temp.children:
                    temp.children[i] = TrieNode()
                temp = temp.children[i]
                temp.count += 1
            temp.end = True
        ans = []
        for word in words:
            temp = head
            s = 0
            for i in word:
                temp = temp.children[i] 
                s += temp.count
            ans.append(s)
        return ans