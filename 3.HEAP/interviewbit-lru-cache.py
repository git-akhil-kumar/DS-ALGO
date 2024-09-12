class DoubleLinkedListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.start = DoubleLinkedListNode() 
        self.end = DoubleLinkedListNode()    
        self.start.next = self.end
        self.end.prev = self.start

    def _remove(self, node: DoubleLinkedListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_end(self, node: DoubleLinkedListNode):
        prev_node = self.end.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.end
        self.end.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_end(node)
            return node.value
        return -1

    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_end(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.start.next
                self._remove(lru_node)
                del self.cache[lru_node.key]
                
            # Create a new node and insert it at the end
            new_node = DoubleLinkedListNode(key, value)
            self._insert_at_end(new_node)
            self.cache[key] = new_node


lru = LRUCache(2)
lru.set(2, 1)
lru.set(1, 1)
lru.set(2, 3)
lru.set(4, 1)
print(lru.get(1))  # Output: -1 (1 was evicted)
print(lru.get(2))  # Output: 3