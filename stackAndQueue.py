# stack: LIFO
# queue: FIFO

class Stack:
	# LIFO
	# End of the list holds the top element of the stack
	def __init__(self):
	    self.items = []

	def isEmpty(self):
	    return self.items == []

	def push(self, item):
	    self.items.append(item)

	def pop(self):
	    return self.items.pop()

	def peek(self):
	    return self.items[len(self.items)-1]

	def size(self):
	    return len(self.items)

class Queue:
	# FIFO
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def HanoiTowers(N):
	"""
	Given 3 towers and N disks, move the disks from tower A to tower C in an
	ascending order, with the restrictions:
	1) only one disk can be moved at a time
	2) a disk is slid off the top of one tower onto the next tower
	3) a disk can only be placed on top of a larger disk
	"""
	assert N > 0
	A = []
	B = []
	C = []
	
	# A [N, N-1, N-2, ..., 1]
	k = N
	while k > 0:
		A.append(k)
		k -= 1
	
	if N == 1:
		x = A.pop(0)
		C.append(x)
		return
	if N == 2:
		B.append(A.pop)

	# and so on

if __name__ == '__main__':
	testStack = Stack()
	testStack.push(0)
	testStack.push(1)
	testStack.push(2)
	testStack.push(3)
	for item in testStack.items:
		print item