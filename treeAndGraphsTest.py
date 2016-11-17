from treeAndGraphs import *

# TESTING FUNCTIONS

def checkBSTTest():
	node2 = Node(-2)
	leftChild = Node(-1, node2)
	node2.setParent(leftChild)
	node1 = Node(-3, None, None, node2)
	node2.setLeftChild(node1)
	rightChild = Node(4)
	rootNode = Node(1, leftChild, rightChild)
	leftChild.setParent(rootNode)
	rightChild.setParent(rootNode)
	print checkBST(rootNode)

def createTree():
	node2 = Node(3)
	leftChild = Node(2, node2)
	node2.setParent(leftChild)
	node1 = Node(-3, None, None, node2)
	node2.setLeftChild(node1)
	rightChild = Node(4)
	rootNode = Node(1, leftChild, rightChild)
	leftChild.setParent(rootNode)
	rightChild.setParent(rootNode)
	return rootNode

def sumPathTest():
	sumPath(createTree(), 3)

def depthTraverseTest():
	print depthTraverse(createTree())

def depthTraverseLinkedListTest():
	array = depthTraverseLinkedList(createTree())
	for head in array:
		head.printNode()
		print "\n"

def linkedListNodePrintTest():
	node8 = LinkedListNode(2)
	node7 = LinkedListNode(9, node8)
	head2 = LinkedListNode(5, node7)
	head2.printNode()

if __name__ == "__main__":
	# sumPathTest()
	# checkBSTTest()
	# depthTraverseTest()
	# linkedListNodePrintTest()
	depthTraverseLinkedListTest()