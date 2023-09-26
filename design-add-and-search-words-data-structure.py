class TrieTree:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TrieTree()

    def addWord(self, word: str) -> None:
        temp = self.head
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieTree()
            temp = temp.children[c] 
        temp.isEnd = True

    def search(self, word: str,temp = None) -> bool:
        if not temp: 
            temp = self.head
        for i,c in enumerate(word):
            if c == ".":
                result = False
                for child in temp.children:
                    result = result or self.search(word[i+1:],temp.children[child])
                return result
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)