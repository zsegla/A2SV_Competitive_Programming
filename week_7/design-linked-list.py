# https://leetcode.com/problems/design-linked-list/



class MyLinkedList:

    def __init__(self):
        self.list = []

    def get(self, index: int) -> int:
        if index >= len(self.list):
            return -1
        return self.list[index]

    def addAtHead(self, val: int) -> None:
        self.list = [val] + self.list

    def addAtTail(self, val: int) -> None:
        self.list.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.list):
            return 
        self.list.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index >= len(self.list):
            return 
        del self.list[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
