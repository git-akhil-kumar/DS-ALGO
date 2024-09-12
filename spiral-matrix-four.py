from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def spiralMatrix(rows: int, cols: int, head: Optional[ListNode]) -> List[List[int]]:
    top, left, right, bottom = 0, 0, cols - 1, rows - 1
    curr = head
    matrix = [[-1 for _ in range(cols)] for _ in range(rows)]

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            if curr:
                matrix[top][col] = curr.val
                curr = curr.next
            else:
                return matrix
        top += 1

        for row in range(top, bottom + 1):
            if curr:
                matrix[row][right] = curr.val
                curr = curr.next
            else:
                return matrix
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                if curr:
                    matrix[bottom][col] = curr.val
                    curr = curr.next
                else:
                    return matrix
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                if curr:
                    matrix[row][left] = curr.val
                    curr = curr.next
                else:
                    return matrix
            left += 1

    return matrix

def createLinkedList(nums):
    head = ListNode(0)
    curr = head
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next

print(spiralMatrix(3, 5, createLinkedList([3,0,2,6,8,1,7,9,4,2,5,5,0])))
