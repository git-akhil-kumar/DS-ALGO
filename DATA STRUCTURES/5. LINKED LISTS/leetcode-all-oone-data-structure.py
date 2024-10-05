from heapq import heapify, heappush


class Dll:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.s = 0
        self.map = {}

        self.max_heap = []
        self.min_heap = []

    def isEmpty(self) -> bool :
        return len(self.max_heap) == 0

    def inc(self, key: str) -> None:
        if key not in self.map :
            heappush(self.max_heap, (-1, key))
            heappush(self.min_heap, (1, key))
            self.map[key] = 1
        else :
            incr = self.map[key]

            max_heap_ele = (-incr, key)
            min_heap_ele = (incr, key)

            self.max_heap.remove(max_heap_ele)
            self.min_heap.remove(min_heap_ele)

            heapify(self.max_heap)
            heapify(self.min_heap)

            heappush(self.max_heap, (-incr-1, key))
            heappush(self.min_heap, (incr+1, key))
            self.map[key] += 1
        print(self.min_heap, self.max_heap)

    def dec(self, key: str) -> None:
        incr = self.map[key]

        max_heap_ele = (-incr, key)
        min_heap_ele = (incr, key)

        self.max_heap.remove(max_heap_ele)
        self.min_heap.remove(min_heap_ele)
        
        heapify(self.max_heap)
        heapify(self.min_heap)

        heappush(self.max_heap, (incr+1, key))
        heappush(self.min_heap, (incr-1, key))

        self.map[key] -= 1 
        print(self.min_heap, self.max_heap)

    def getMaxKey(self) -> str:
        return "" if self.isEmpty() else self.max_heap[0][1]
        

    def getMinKey(self) -> str:
        return "" if self.isEmpty() else self.min_heap[0][1]


tests = [["AllOne","inc","inc","inc","inc","inc","dec","dec","getMaxKey","getMinKey"],[[],["a"],["b"],["b"],["b"],["b"],["b"],["b"],[],[]]]
for i in range(len(tests)//2):
    n = len(tests[i])

    obj = AllOne()
    for k in range(1, n):
        key = tests[i][k]
        val = tests[i+1][k]

        if key == "inc":
            obj.inc(val[0])
        
        if key == "getMaxKey":
            print(obj.getMaxKey()) 

        if key == "getMinKey":
            print(obj.getMinKey())
