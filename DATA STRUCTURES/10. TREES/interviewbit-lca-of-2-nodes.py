
from collections import deque


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def path_to_node(root, node) :
    if not root :
        return []
    if root.val == node :
        return [root.val]
    
    left = path_to_node(root.left, node)
    right = path_to_node(root.right, node)

    if left :
        return left + [root.val]
    if right :
        return right + [root.val]
    return []
    
def lca_method_2(root, nodeA, nodeB) :
    if not root :
        return None
    if root.val == nodeA or root.val == nodeB :
        return root
    path_to_a = path_to_node(root, nodeA)
    path_to_b = path_to_node(root, nodeB)
    lca_node = -1
    for a, b in zip(path_to_a, path_to_b) :
        if a != b :
            break
        lca_node = a
    return lca_node

def lca(root, nodea, nodeb) :  
    if not root :
         return None
    if root.val == nodea or root.val == nodeb :
        return root
    left = lca(root.left, nodea, nodeb)
    right = lca(root.right, nodea, nodeb)
    if left and right :
        return root
    return left or right

def createTree(nums):
    n = len(nums)
    i = 0
    root = TreeNode(nums[i])
    curr = None
    while i < n :
        curr = root if curr is None else TreeNode(nums[i])
        left_child_idx, right_child_idx = (2 * i) + 1, (2 * i) + 2

        if left_child_idx < n and nums[left_child_idx] != -1:
            curr.left = TreeNode(nums[left_child_idx])
        if right_child_idx < n and nums[right_child_idx] != -1:
            curr.right = TreeNode(nums[right_child_idx])
        i += 1
        
    return root

def levelOrderTraversal(root):
    queue = deque()
    queue.append(root)
    levels = []
    while len(queue) > 0 :
        size = len(queue)
        curr_level = []
        for _ in range(size):
            node = queue.popleft()
            curr_level.append(node.val)
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        levels.append(curr_level)

    return levels
             
def inorder(root):
    if not root :
        return 
    inorder(root.left)
    inorder(root.right)
          


nums = [1,2,3]
root = createTree(nums)
node_a = 2
node_b = 3

print(lca(root, node_a, node_b))

