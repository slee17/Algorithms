class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, new_next):
        self.nextNode = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

def kthToLast(head, k):
	"""
	Returns the kth last element of a singly linked list whose head is head.
	"""
	advancedK = head
	for i in range(k-1):
		advancedK = advancedK.nextNode
	isEnd = False
	while not isEnd:
		advancedK = advancedK.nextNode
		head = head.nextNode
		if advancedK.nextNode == None:
			isEnd = True
	return head.data

def deleteMiddle(current):
	"""
	Deletes the middle node of a linked list, given only access to that node.
	"""
	# debug
	assert current != None

	nextNode = current.nextNode
	current.data = nextNode.data
	current.next = nextNode.nextNode
	"""
	while current.nextNode != None:
		nextNode = current.nextNode
		current.data = nextNode.data
		current.next = nextNode.nextNode
		current = current.nextNode
	"""
	return

def partitionLinkedList(head, x):
	"""
	Partitions a linked list around x, such that all nodes less than x come
	before all nodes greater than or equal to x.
	"""
	# come back to this
	assert head != None
	
	# make a tail pointer, get the size of the linked list
	size = 1
	tail = head
	while tail.nextNode != None:
		size += 1
		tail = tail.nextNode

	copy = head
	for i in range(size):
		if copy.data > x:
			# put it at the tail
			tail.nextNode = copy
			copy = tail

	"""
	# make a dummy node that precedes the head
	# i.e. copy - head - node1 - node2 - ...
	copy = Node(None, head)
	for i in range(size):
		if copy.nextNode.data > x
			tail.nextNode = Node(copy.nextNode.data)
			copy.nextNode = copy.nextNode.nextNode
		copy = copy.nextNode
	"""

	# traverse the linked list, changing head and tail as necessary
	# i.e. if value > x, make it the new tail, reset head to the next node
	# if value <= x, we are good

	# return the new head
	return head

if __name__ == "__main__":
	# Creating a linked list.
	node5 = Node(0)
	node4 = Node(1, node5)
	node3 = Node(2, node4)
	node2 = Node(3, node3)
	node1 = Node(4, node2)
	head = Node(5, node1)
	testList = LinkedList(head)
	
	#deleteMiddle(node3)
	#print kthToLast(head, 3)
	
	partitionLinkedList(head, 3)

	copy = head
	while copy != None:
		print copy.data, "-",
		copy = copy.nextNode


