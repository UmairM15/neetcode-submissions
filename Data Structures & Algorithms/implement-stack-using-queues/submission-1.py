class MyStack:

    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        temp = deque()
        for _ in range(len(self.deque) - 1):
            temp.append(self.deque.popleft())
        val = self.deque.popleft()
        for _ in range(len(temp)):
            self.deque.append(temp.popleft())
        return val

    def top(self) -> int:
        temp = deque()
        for _ in range(len(self.deque) - 1):
            temp.append(self.deque.popleft())
        val = self.deque[0]
        temp.append(self.deque.popleft())
        for _ in range(len(temp)):
            self.deque.append(temp.popleft())
        return val

    def empty(self) -> bool:
        return len(self.deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()