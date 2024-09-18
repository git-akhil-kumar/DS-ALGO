# url :- https://leetcode.com/problems/implement-trie-prefix-tree/description/


from abc import ABC, abstractmethod


class TrieNode:
    def __init__(self, char):
        self.val = char
        self.edges = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word :
            if char not in curr.edges :
                curr.edges[char] = TrieNode(char)
            curr = curr.edges[char]
        curr.is_word_end = True

    def search(self, word: str) -> bool:
        curr = self.root 
        for char in word :
            if char not in curr.edges:
                return False 
            curr = curr.edges[char]
        return curr.is_word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix :
            if char not in curr.edges:
                return False 
            curr = curr.edges[char]
        return True
    

# Strategy pattern 

class TrieOperation(ABC): # strategy
    @abstractmethod
    def execute(self, trie, value):
        pass

class InitializationOperation(TrieOperation): # discreate strategy
    def execute(self, trie, value):
        return None

class InsertOperation(TrieOperation):
    def execute(self, trie, value):
        trie.insert(value[0])
        return None

class SearchOperation(TrieOperation):
    def execute(self, trie, value):
        return trie.search(value[0])

class StartsWithOperation(TrieOperation):
    def execute(self, trie, value):
        return trie.startsWith(value[0])

class TrieContext: # context
    def __init__(self):
        self.trie = Trie()
        self.operations = {
            "Trie": InitializationOperation(),
            "insert": InsertOperation(),
            "search": SearchOperation(),
            "startsWith": StartsWithOperation()
        }

    def execute_operation(self, operation, value):
        return self.operations[operation].execute(self.trie, value)

# Usage
operations = ["Trie","insert","search","search","startsWith","insert","search"]
values = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

context = TrieContext()
results = []

for operation, value in zip(operations, values):
    result = context.execute_operation(operation, value)
    results.append(result)

print(results == [None,None,True,False,True,None,True])