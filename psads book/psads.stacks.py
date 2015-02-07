# Playing with stacks and stack functions.
# Following the book: Problem Solving with Algorithms
#   and Data Structures using Python

class Stack:
	def __init__(self):
		self.items = []
		print self.items

	def is_empty(self):
		print "is empty? ", self.items == []
		return self.items == []

	def push(self, item):
		print "adding this: ", item
		return self.items.append(item)

	def pop(self):
		if self.items != []:
			# print "popping this: ", self.items.pop(-1)
			return self.items.pop()
		else:
			pass

# Peek is just a matter of peeking at the top of the stack
# without changing the stack (unlike pop, which removes)

	def peek(self):
		print "peeking at: ", self.items[len(self.items)-1]
		return self.items[len(self.items)-1]

s=Stack()

s.is_empty()
s.push(34)
s.push(38)
s.push(383)
print "the stack: ", s.items
s.is_empty()
s.pop()
s.pop()
s.is_empty()
print "the stack: ", s.items
s.pop()
s.is_empty()
print "the stack: ", s.items

s.push(3433)
s.push(23212)
s.push(343)
s.peek()

stack=Stack()
stack.push("(")
# stack.push("(")
# stack.push("(")
stack.push(")")
print stack.items

def balanced_parens(stack):
	# balanced = True
	# print stack.items
	new_stack = Stack()
	for item in stack.items:
		print item
		if item=="(":
			new_stack.push("(")
		if item==")":
			new_stack.pop()
	print "stack is: ", new_stack.items
	if len(new_stack.items) > 0:
		balanced = False
	else:
		balanced = True
	print balanced

balanced_parens(stack)



