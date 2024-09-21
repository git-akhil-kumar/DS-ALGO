class DoublyLinkedList:
    def __init__(self, key = None, value = None, prev = None, next = None) :
        self.key    = key 
        self.value  = value 
        self.prev   = prev
        self.next   = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map      = dict()
        self.start    = DoublyLinkedList()   # Dummy node to the start of the list
        self.end      = DoublyLinkedList()   # Dummy node to the end of the list
        self.start.next = self.end 
        self.end.prev   = self.start

    def remove(self, node): 
        prev_node      = node.prev
        next_node      = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_at_end(self, node: DoublyLinkedList):
        last_node      = self.end.prev
        last_node.next = node 
        node.prev      = last_node
        node.next      = self.end 
        self.end.prev  = node

    def get(self, key):
        if key in self.map :
            node: DoublyLinkedList = self.map[key]
            self.remove(node)
            self.insert_at_end(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.map :
            node = self.map[key]
            self.remove(node)
            self.insert_at_end(node)
            node.value = value
        else :
            if len(self.map) >= self.capacity :
                lru_node = self.start.next
                del self.map[lru_node.key]
                self.remove(lru_node)

            new_node = DoublyLinkedList(key, value)
            self.map[key] = new_node
            self.insert_at_end(new_node)
            

lru = LRUCache(2)

lru.set(2, 1)
lru.set(1, 1)
lru.set(2, 3)
lru.set(4, 1)
print(lru.get(1))  # Output: -1 (1 was evicted)
print(lru.get(2))  # Output: 3
