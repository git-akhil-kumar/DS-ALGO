# Reverse a linked list using recursion.
# Example :
#  Given 1->2->3->4->5->NULL,
# return 5->4->3->2->1->NULL.
# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
def createLinkedList(nums) :
	head = ListNode(0)
	curr = head
	for num in nums :
		curr.next = ListNode(num) # type: ignore
		curr = curr.next # type: ignore
	return head.next

def printLinkedList(head):
	while head :
		print(head.val, end=" ")
		head = head.next

def reverseList(head):
	if not head or not head.next :
		return head
	prev = head 
	start = head 
	curr = head 
	while curr :
		print(curr.val, end=" ")
		next = curr.next 
		prev.next = next 
		curr.next = start 
		start = curr 
		curr = next
	print()
	return start


nums = [1, 2]
head = reverseList(createLinkedList(nums))
printLinkedList(head)
print()