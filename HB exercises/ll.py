class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def AddNode(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node

		if self.tail != None:
			self.tail.next = new_node

		self.tail = new_node

	def PrintList(self):
		node = self.head
		print "This is the whole list: "
		while node != None:
			print node.data
			node = node.next
		print "-----------------"

	def FindTwo(self):
		node = self.head
		counter = 1
		while node != None:
			print node.data
			if node.data == 2:
				print "Found 2 at position:", counter
			node = node.next
			counter = counter + 1
		print "----------------"

	def DeleteTwo(self):
		node = self.head
		previous = None
		found = False
		while not found:
			if node.data == 2:
				found = True
			elif node.data is None:
				raise ValueError("Node not in linked list")
			else:
				previous = node
				node =  node.next
		if previous is None:
			self.head = node.next
		else:
			previous.next = node.next

	def CountList(self):
		node = self.head
		count = 1
		while node != None:
			node = node.next
			count = count + 1
		# print "This is the list length: ", count
		# print "----------------"
		return count

	def nthMemberfromHead(self, nth):
		node = self.head
		counter = 1
		print "This is the nth: ", nth
		# while node != None:
		while counter != nth:
			counter = counter + 1
			node = node.next
		print "This is the nth member: ", node.data
		print "----------------"

	def nthMemberfromTail(self, nth):
		# print "This is the nth input; nth from tail: ", nth
		node = self.head
		l.CountList()
		# print l.CountList()
		nth = l.CountList() - nth
		counter = 1
		# print "This is the nth: ", nth
		# while node != None:
		while counter != nth:
			counter = counter + 1
			node = node.next
		print "This is counting back from the tail: ", node.data
		print "----------------"



l = LinkedList()
l.AddNode(1)
l.AddNode(2)
l.AddNode(3)
l.AddNode(4)
l.AddNode("Cat")
l.AddNode(6)
l.AddNode(7)
l.AddNode(8)

l.CountList()
l.FindTwo()
l.DeleteTwo()
l.PrintList()
l.nthMemberfromHead(6)
l.nthMemberfromTail(7)
