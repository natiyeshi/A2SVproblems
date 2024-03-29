class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.que = deque()
    def enQueue(self, value: int) -> bool:
        if len(self.que) >= self.k:
            return False
        self.que.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.que) == 0: 
            return False
        self.que.popleft()
        return True

    def Front(self) -> int:
        if len(self.que) < 1:
            return -1
        return self.que[0]

    def Rear(self) -> int:
        if len(self.que) < 1:
            return -1
        return self.que[-1]

    def isEmpty(self) -> bool:
        return False if len(self.que) != 0 else True        

    def isFull(self) -> bool:
        return True if len(self.que) == self.k else False        

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()