
from collections import deque


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def lca(root, nodea, nodeb) :  
    return 0

nums = [1,2,3,-1,-1,4,-1,-1,5,-1,-1]
node_a = 31
node_b = 39

def createTree(nums):
    n = len(nums)
    i = 0
    root = TreeNode(nums[i])
    curr = None
    while i < n :
        curr = root if curr is None else TreeNode(nums[i])
        left_child_idx, right_child_idx = (2 * i) + 1, (2 * i) + 2

        print('root', i, 'left_child_idx', left_child_idx, 'right_child_idx', right_child_idx)
        if left_child_idx < n and nums[left_child_idx] != -1:
            print('creating left child', i, nums[left_child_idx])
            curr.left = TreeNode(nums[left_child_idx])
        if right_child_idx < n and nums[right_child_idx] != -1:
            print('creating right child',i, nums[right_child_idx])
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
    print('level order', root.val)
    inorder(root.right)
          
root = createTree(nums)
print(levelOrderTraversal(root))
inorder(root)
print(lca(root, node_a, node_b))

