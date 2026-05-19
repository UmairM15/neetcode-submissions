class Node:
    def __init__(self, data, node):
        self.data = data
        self.next = node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if (index < 0 or index >= self.length):
            return -1

        curnode = self.head
        for i in range(index):
            curnode = curnode.next

        return curnode.data

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1

    def insertTail(self, val: int) -> None:
        if (self.length == 0):
            self.insertHead(val)
            return

        curnode = self.head
        for i in range(self.length - 1):
            curnode = curnode.next
        
        curnode.next = Node(val, None)
        self.length += 1

    def remove(self, index: int) -> bool:
        if (index < 0 or index >= self.length):
            return False

        self.length -= 1

        if (index == 0):
            self.head = self.head.next
            return True

        curnode = self.head
        for i in range (index - 1):
            curnode = curnode.next
        curnode.next = curnode.next.next

        return True

    def getValues(self) -> List[int]:
        arr = []
        if (self.length == 0):
            return arr

        curnode = self.head
        arr.append(curnode.data)

        for i in range (self.length - 1):
            curnode = curnode.next
            arr.append(curnode.data)

        return arr

        
