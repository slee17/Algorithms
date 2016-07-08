"""Bellman-Ford.py
Five different mplementations of the Bellman-Ford algorithm:

This algorithm computes shortest paths from a single source vertex to all the other
vertices in a weighted graph. The runtime of this algorithm is O(VE), given the
graph has V vertices and E edges.

All five implementations return False when the graph contains a negative cycle."""

__author__ = "Rachel Lee"

from collections import deque

graph = {}
V = set() # set of all vertices in the graph

def buildVertexSet(edgeList):
	"""Takes in an array of edges represented in tuples of (start node, end node, edge weight)
	and returns a set of all vertices in the graph.
	"""
	global V
	V = set()

	for edge in edgeList:
		V.update(edge[:2])

	return V

def buildGraph(edgeList):
	"""Takes in an array of edges represented in tuples of (start node, end node, edge weight)
	and returns a hash table whose keys are all nodes in the graph, and whose
	values are tuples of (end node, edge weight) for each outgoing edge of the key.

	For instance, if the given graph has edges (1, 2, 1), (2, 3, 5), (4, 2, 6), and (4, 3, 4),
	this function will return {1: [(2, 1)], 2: [(3, 5)], 3: [], 4: [(2, 6), (3, 4)]}."""
	global graph
	graph = {}

	# initialize our dictionary
	for v in V:
		graph.setdefault(v, [])

	# fill in the values appropriately
	for edge in edgeList:
		graph[edge[0]].append(edge[1:])

	return graph

def a(G, s):
	"""The basic algorithm.

	Sets the source's distance to 0 and all other distances to infinity.
	Repeat "relax all the edges" V-1 times.

	@param G Graph in a form of a dictionary
	@param s The source node, represented as a number between 1 and V"""
	
	# note that dist[0] and prev[0] are simply placeholders
	dist = [float("inf")] * (max(V)+1)
	prev = [None] * (max(V)+1)

	dist[s] = 0
	for i in range(len(V)-1): # repeat V-1 times
		for v in V: # iterate over all vertices
			for e in graph[v]: # iterate over all outgoing edges from vertex v
				u = e[0]
				w = e[1]
				if dist[u] > dist[v] + w:
					dist[u] = dist[v] + w
					prev[u] = v

	# check for negative cycles
	# if we can do even better with another iteration, then there exists a negative cycle
	for v in V:
		for e in graph[v]:
			# relax all the edges
			u = e[0]
			w = e[1]
			if dist[u] > dist[v] + w:
				return False

	return dist[1:] # return shortest paths to each vertex from the source

def b(G, s):
	"""The basic algorithm with an early-stopping rule.

	Sets the source's distance to 0 and all other distances to infinity.
	Repeat "relax all the edges" until we have repeated V-1 times or a
	"relax all the edges" pass was performed without changing any node distances.

	@param G Graph in a form of a dictionary
	@param s The source node, represented as a number between 1 and V"""
	
	# note that dist[0] and prev[0] are simply placeholders
	dist = [float("inf")] * (max(V)+1)
	prev = [None] * (max(V)+1)

	dist[s] = 0
	repeat = True
	i = 1
	while i < len(V) and repeat:
		repeat = False
		for v in V: # iterate over all vertices
			for e in graph[v]: # iterate over all outgoing edges from vertex v
				u = e[0]
				w = e[1]
				if dist[u] > dist[v] + w:
					dist[u] = dist[v] + w
					prev[u] = v
					repeat = True
		i += 1

	# check for negative cycles
	# if we can do even better with another iteration, then there exists a negative cycle
	for v in V:
		for e in graph[v]:
			# relax all the edges
			u = e[0]
			w = e[1]
			if dist[u] > dist[v] + w:
				return False

	return dist[1:] # return shortest paths to each vertex from the source

def c(G, s):
	"""A more sophisticated version that uses a queue of nodes.

	Set the source' distance to 0 and all other distances to infinity.
    Create a queue of nodes, initially containing just the source node.
    Repeat the following steps until the queue is empty:
    	- Dequeue a node v;
		- For all edges that start at v: relax the edge, and if the best distance
          to the target w of the edge is thereby decreased, enqueue w."""
	# initialize dist - note that dist[0] is simply a placeholder
	dist = [float("inf")] * (max(V)+1)
	prev = [None] * (max(V)+1)

	dist[s] = 0

	# initialize queue of nodes
	queue = deque()
	queue.append(s)
	
	while len(queue) > 0:
		v = queue.popleft()
		for e in graph[v]: # iterate over all outgoing edges from v
			u = e[0]
			w = e[1]
			if dist[u] > dist[v] + w:
				dist[u] = dist[v] + w
				prev[u] = v
				queue.append(u)

	return dist[1:]

def d(G, s):
	"""The same queue-based algorithm as above, but before enqueuing any node,
    we check in Theta(1) time that it's not already in the queue; if it is in
    the queue, we don't add it a second time.

	Set the source' distance to 0 and all other distances to infinity.
    Create a queue of nodes, initially containing just the source node.
    Repeat the following steps until the queue is empty:
    	- Dequeue a node v;
		- For all edges that start at v: relax the edge, and if the best distance
          to the target u of the edge is thereby decreased, and if u is not already
          in the queue, enqueue u."""
	# initialize dist - note that dist[0] is simply a placeholder
	dist = [float("inf")] * (max(V)+1)
	prev = [None] * (max(V)+1)

	dist[s] = 0

	# initialize queue of nodes
	queue = deque()
	queue.append(s)
	
	# inQueue is an array for searching if the node u is currently in the queue
	# if the node u is in the queue, then inQueue[u] = True, otherwise False
	# supports Theta(1) search
	inQueue = [False] * (max(V)+1) # inQueue[0] is simply a placeholder

	while len(queue) > 0:
		v = queue.popleft()
		inQueue[v] = False
		for e in graph[v]: # iterate over all outgoing edges from v
			u = e[0]
			w = e[1]
			if dist[u] > dist[v] + w:
				dist[u] = dist[v] + w
				prev[u] = v
				if not inQueue[u]:
					queue.append(u)
					inQueue[u] = True

	return dist[1:]

def e(G, s):
	"""The same algorithm as above, but using a stack instead of a queue.

	Set the source' distance to 0 and all other distances to infinity.
    Create a stack of nodes, initially containing just the source node.
    Repeat the following steps until the stack is empty:
    	- Pop a node v from the stak;
		- For all edges that start at v: relax the edge, and if the best distance
          to the target u of the edge is thereby decreased, and if u is not already
          in the stack, add u to the stack."""
	# initialize dist - note that dist[0] is simply a placeholder
	dist = [float("inf")] * (max(V)+1)
	prev = [None] * (max(V)+1)

	dist[s] = 0

	# initialize stack of nodes
	stack = []
	stack.append(s)
	
	# inStack is an array for searching if the node u is currently in the stack
	# if the node u is in the stack, then inStack[u] = True, otherwise False
	# supports Theta(1) search
	inStack = [False] * (max(V)+1) # inStack[0] is simply a placeholder

	while len(stack) > 0:
		v = stack.pop()
		inStack[v] = False
		for e in graph[v]: # iterate over all outgoing edges from v
			u = e[0]
			w = e[1]
			if dist[u] > dist[v] + w:
				dist[u] = dist[v] + w
				prev[u] = v
				if not inStack[u]:
					stack.append(u)
					inStack[u] = True

	return dist[1:]