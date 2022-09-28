# https://leetcode.com/problems/implement-queue-using-stacks/submissions/



class MyQueue:

    def __init__(self):
        self.stack = []
        self.reversed = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.top = x
        self.stack.append(x)
        
    def pop(self) -> int:
        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()

    def peek(self) -> int:
        if  self.reversed:
            return self.reversed[-1]
        return self.top

    def empty(self) -> bool:
        return not self.stack and not self.reversed


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
