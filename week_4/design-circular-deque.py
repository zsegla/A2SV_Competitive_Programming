# https://leetcode.com/problems/design-circular-deque/submissions/



class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k +1 
        self.q = [None] * self.k
        self.head = self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head + 1) % self.k
        self.q[self.head] = value
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail - 1) % self.k
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head - 1) % self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail +1) % self.k]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.head + 1)%self.k == self.tail 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
