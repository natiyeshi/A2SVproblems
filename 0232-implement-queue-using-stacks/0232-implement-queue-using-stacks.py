class MyQueue:

    def __init__(self):
        self.que = []
        self.front = 0
    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        self.front += 1
        return self.que[self.front - 1]

    def peek(self) -> int:
        return self.que[self.front]
        
    def empty(self) -> bool:
        if len(self.que) == self.front:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()