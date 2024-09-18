
class TrieNode:
    def __init__(self, char) -> None:
        self.val = char
        self.edges = {}
        self.is_word_end = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode(None) # reference to the head
    
    def _insert(self, word):
        curr = self.root 
        for char in word :
            if char not in curr.edges :
                curr.edges[char] = TrieNode(char)

            curr = curr.edges[char]
        
        curr.is_word_end = True

    def _search(self, word) -> bool :
        curr = self.root 
        for i in range(len(word)) :
            char = word[i]
            if char not in curr.edges :
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

    def _delete(self, word):
        self._delete_recursive(self.root, word, 0)
    
    def _delete_recursive(self, node, word, depth):
        if not node:
            return False
        
        if depth == len(word):
            if node.is_word_end:
                node.is_word_end = False
                return len(node.edges) == 0
            return False
        
        char = word[depth]
        if char not in node.edges:
            return False
        
        should_delete_curr_node = self._delete_recursive(node.edges[char], word, depth + 1)

        if should_delete_curr_node:
            del node.edges[char]
            return not node.is_word_end and len(node.edges) == 0
        
        return False
    

trie = Trie()
trie._insert("WHERE")
trie._insert("WHY")
trie._insert("WHAT")

print(trie._search("WHY"))