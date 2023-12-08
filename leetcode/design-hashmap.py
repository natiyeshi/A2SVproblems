class MyHashMap:

    def __init__(self):
        self.capacity = 100
        self.ind = [-1] * 100        

    def put(self, key: int, value: int) -> None:
        
        if key >= self.capacity:
            space = key - self.capacity + 2
            self.capacity += space
            self.ind.extend([-1] * space )
        self.ind[key] = value

    def get(self, key: int) -> int:
        if key >= self.capacity:
            return -1
        return self.ind[key]
        

    def remove(self, key: int) -> None:
        if key >= self.capacity:
            return
        self.ind[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)