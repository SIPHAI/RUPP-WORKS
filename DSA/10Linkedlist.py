# Python program for traversal of a linked list
# Node class


class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next


# Code execution starts here
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)
	fifth = Node(5)
	sixth = Node(6)
	seventh = Node(7)
	eighth = Node(8)
	ninth = Node(9)
	tenth = Node(10)

	llist.head.next = second # Link first node with second
	second.next = third # Link second node with the third node
	third.next = fourth # Link third node with the fourth node
	fourth.next = fifth # Link fourth node with the fifth node
	fifth.next = sixth # Link fifth node with the sixth node
	sixth.next = seventh # Link sixth node with the seventh node
	seventh.next = eighth # Link seventh node with the eighth node
	eighth.next = ninth # Link eighth node with the ninth node
	ninth.next = tenth # Link ninth node with the tenth node
    

	llist.printList()
