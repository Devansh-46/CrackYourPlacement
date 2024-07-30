# Python code to rearrange linked list in zig zag fashion

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None


# This function distributes the Node in zigzag fashion
def zigZagList(head):

	# If flag is true, then next node should be greater
	# in the desired output.
	flag = True

	# Traverse linked list starting from head.
	current = head
	while (current.next != None):
	
		if (flag): # "<" relation expected
		
			# If we have a situation like A > B > C
			# where A, B and C are consecutive Nodes
			# in list we get A > B < C by swapping B
			# and C 
			if (current.data > current.next.data):
				t = current.data
				current.data = current.next.data
				current.next.data = t
			
		
		else :# ">" relation expected
		
			# If we have a situation like A < B < C where
			# A, B and C are consecutive Nodes in list we
			# get A < C > B by swapping B and C 
			if (current.data < current.next.data):
				t = current.data
				current.data = current.next.data
				current.next.data = t
			
		current = current.next
		if(flag):
			flag = False # flip flag for reverse checking 
		else:
			flag = True
	return head

# function to insert a Node in 
# the linked list at the beginning.
def push(head, k):

	tem = Node(0)
	tem.data = k
	tem.next = head
	head = tem
	return head

# function to display Node of linked list.
def display( head):

	curr = head
	while (curr != None): 
		print( curr.data, "->", end =" ")
		curr = curr.next
	
	print("None")

# Driver code

head = None

# create a list 4 -> 3 -> 7 -> 8 -> 6 -> 2 -> 1
# answer should be -> 3 7 4 8 2 6 1
head = push(head, 1)
head = push(head, 2)
head = push(head, 6)
head = push(head, 8)
head = push(head, 7)
head = push(head, 3)
head = push(head, 4)

print("Given linked list \n")
display(head)

head = zigZagList(head)

print("\nZig Zag Linked list \n")
display(head)
