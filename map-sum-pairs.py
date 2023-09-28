class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.val = 0

class MapSum:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.head
        for i in key:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.end = True
        node.val = val
    def findSum(self,node):
        s = node.val
        for i in node.children:
            s += self.findSum(node.children[i])
        return s
    def sum(self, prefix: str) -> int:
        node = self.head
        for i in prefix:
            if i not in node.children:
                return 0
            node = node.children[i]
        return self.findSum(node)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)