from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next:
        return head
    odd_last, even_last, curr_node = head, head.next, head.next.next
    while curr_node and even_last :
        curr_node_next = curr_node.next
        even_first = odd_last.next
        odd_last.next = curr_node
        odd_last = curr_node
        odd_last.next = even_first

        even_last.next = curr_node_next
        even_last = curr_node_next
        if not curr_node_next :
            break
        curr_node = even_last.next
    return head


def create_linked_list(nums):
    curr = ListNode(0)
    head = curr
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def print_ll(node: Optional[ListNode]):
    s = ""
    while node:
        s += str(node.val) + " "
        node = node.next
    print(s)


ll = create_linked_list([2, 3, 4])
print_ll(ll)
print("- - - - - - - - - -")
print_ll(oddEvenList(ll))
