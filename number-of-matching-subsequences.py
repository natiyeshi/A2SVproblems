class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
        self.count = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        head = TrieNode()
        for word in words:
            node = head
            for c in word:
                ind = ord(c) - ord('a')
                if not node.children[ind]:
                    node.children[ind] = TrieNode()
                node = node.children[ind]
            node.end = True
            node.count += 1
        def findindex(word,ch,start):
            for i in range(start,len(word)):
                if ch == word[i]:
                    return i
            return -1
        ans = 0
        def dfs(node,word,index = 0):
            nonlocal ans
            for i in range(26):
                if node.children[i]:
                    child = node.children[i]
                    ind = findindex(word,chr(i + ord('a')),index)
                    if ind != -1:
                        if child.end:
                            ans += child.count
                        dfs(child,word,ind + 1)
           
        dfs(head,s)
        
        return ans