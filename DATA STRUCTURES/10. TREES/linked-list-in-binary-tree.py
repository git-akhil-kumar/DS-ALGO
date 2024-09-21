class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def isSubPath(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
#     if not head:
#         return True

#     llhead = head

#     def rec(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
#         nonlocal llhead

#         if not head:
#             return True
#         if not root:
#             return False

#         if root.val == head.val:
#             if head.next:
#                 if (
#                     root.left
#                     and root.left.val == head.next.val
#                     and rec(head.next, root.left)
#                 ):
#                     return True

#                 if (
#                     root.right
#                     and head.next.val == root.right.val
#                     and rec(head.next, root.right)
#                 ):
#                     return True

#                 return rec(llhead, root.left) or rec(llhead, root.right)
#             else:
#                 return True

#         return rec(llhead, root.left) or rec(llhead, root.right)

#     return rec(head, root)


def createLinkedList(nums):
    head = ListNode(0)
    it = head
    for num in nums:
        it.next = ListNode(num)
        it = it.next
    return head.next


def printLinkedList(head):
    while head:
        print(head.val)
        head = head.next


def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is None:
            return None

        print("index", i, "values", arr[i])

        # Create a new node with the current element
        temp = TreeNode(arr[i])
        root = temp

        # Recursively insert left and right children
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)

        return root

    return root


def createBinaryTree(arr):
    n = len(arr)
    return insertLevelOrder(arr, None, 0, n)


def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)


llArr = [1, 4, 2, 6, 8]
head = createLinkedList(llArr)
# printLinkedList(head)

treeArr = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
root = createBinaryTree(treeArr)
inorderTraversal(root)
# print(isSubPath(head, root))
