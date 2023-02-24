class DataStream:

    def __init__(self, value: int, k: int):
        self.arr = deque()
        self.value = value
        self.k = k
        self.counter = k
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.counter = self.k
        else:
            if self.counter > 0:self.counter -= 1
        if len(self.arr) == self.k:
            self.arr.popleft()
        self.arr.append(num)
        if len(self.arr) == self.k and self.counter == 0:
            return True 
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)