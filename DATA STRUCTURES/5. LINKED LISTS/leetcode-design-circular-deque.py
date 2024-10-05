class CircularDeque:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k

        self.start = CircularDeque(None)
        self.end = CircularDeque(None)

        self.start.next = self.end
        self.end.prev = self.start
        

    def insertFront(self, value: int) -> bool:
        if self.isFull() :
            return False

        first_node = self.start.next 
        new_node = CircularDeque(value)
        self.start.next = new_node
        new_node.prev = self.start
        new_node.next = first_node
        first_node.prev = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        last_node = self.end.prev
        new_node = CircularDeque(value)
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.end
        self.end.prev = new_node
        self.size += 1
    
        return True

        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False 
        
        first_node = self.first.next 
        second_node = first_node.next
        self.first.next = second_node
        second_node.prev = self.first
        del first_node
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        last_node = self.end.prev
        second_last_node = last_node.prev
        second_last_node.next = self.end
        self.end.prev = second_last_node
        self.size -= 1
        del last_node
        return True
        

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.start.next.val
        

    def getRear(self) -> int:
        if self.size == 0 :
            return -1
        return self.end.prev.val
        
    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size >= self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# ["MyCircularDeque",
# "insertLast",
# "insertLast",
# "insertFront",
# "insertFront",
# "getRear",
# "isFull",
# "deleteLast",
# "insertFront",
# "getFront"]
obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())

