# linked list review
# create a linked list and add node fast as you can

# Node

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None




# List

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node

		if self.tail != None:
			self.tail.next = new_node

		self.tail = new_node

l = LinkedList()
l.add_node(5)
l.add_node(89)
l.add_node(3)

print l.head.data
print l.head.next.data
print l.head.next.next.data
print l.tail.data
