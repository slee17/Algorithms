"""BellmanFord_test.py
File for testing implentations of Bellman-Ford algorithm in BellmanFord.py.

IMPORTANT
	In order to run this script, you will have to first download NetworkX.
	One way to do this is to run `pip install networkx` in the command line.
	https://networkx.github.io/documentation/latest/reference/introduction.html

COMMAND-LINE USAGE
   python BellmanFord_test.py runs all the necessary tests (including tests for correctness
	and running time).

Tests use various sizes and kinds of graphs: small, medium, large, and
sparse, dense, in-between.
"""

from BellmanFord import *
import networkx as nx # for generating random graphs
import random # for generating random graphs
import sys, time # for testing

SOURCE = 1
WEIGHTRANGE = (-10, 20)
global graph, V

def generateRandomGraph(n, p):
	"""Function for generating a random directed graph.
	@param n the number of nodes in int
	@param p probability for edge creation in float"""
	g = nx.gnp_random_graph(n, p, directed=True)
	edgeList = []
	global WEIGHTRANGE

	source = float("inf")

	for edge in g.edges():
		if edge[0] > 0 and edge[1] > 0:
			weight = random.randint(WEIGHTRANGE[0], WEIGHTRANGE[1]) # generate random weight
			edgeList.append(edge + (weight,))  # randomly assign edge weight to each edge
			if edge[0] < source or edge[1] < source:
				source = min(edge[0], edge[1])

	if len(edgeList) == 0:
		edgeList = [(1, 3, 5)]
		source = 1

	return (edgeList, source)

def timeA(G, s):
	sys.stdout.flush()  # make sure the previous line is displayed now,
						# rather than waiting for the end-of-line character

	start = time.clock()    # start the timer
	result = a(G, s)
	end = time.clock()      # stop the timer

	elapsed = end - start
	print elapsed, " seconds"
	return result

def timeB(G, s):
	sys.stdout.flush()  # make sure the previous line is displayed now,
						# rather than waiting for the end-of-line character

	start = time.clock()    # start the timer
	result = b(G, s)
	end = time.clock()      # stop the timer

	elapsed = end - start
	print elapsed, " seconds"
	return result

def timeC(G, s):
	sys.stdout.flush()  # make sure the previous line is displayed now,
						# rather than waiting for the end-of-line character

	start = time.clock()    # start the timer
	result = c(G, s)
	end = time.clock()      # stop the timer

	elapsed = end - start
	print elapsed, " seconds"
	return result

def timeD(G, s):
	sys.stdout.flush()  # make sure the previous line is displayed now,
						# rather than waiting for the end-of-line character

	start = time.clock()    # start the timer
	result = d(G, s)
	end = time.clock()      # stop the timer

	elapsed = end - start
	print elapsed, " seconds"
	return result

def timeE(G, s):
	sys.stdout.flush()  # make sure the previous line is displayed now,
						# rather than waiting for the end-of-line character

	start = time.clock()    # start the timer
	result = e(G, s)
	end = time.clock()      # stop the timer

	elapsed = end - start
	print elapsed, " seconds"
	return result
	
def process(arguments):
	"""Process the command-line, and run appropriate test routines."""
	sizeL = ["small", "medium", "large"]
	nList = [(1, 5), (8, 11), (15, 20)]
	graphL = ["sparse", "balanced", "dense"]
	pList = [(0.10, 0.20), (0.21, 0.40), (0.50, 0.60)]

	global graph, V

	if len(sys.argv) == 1:
		# no command-line arguments other than the name of this python program
		# runs the default tests, which is composed of correctness tests and time tests
		# on randomly generate graphs
		for sizeType in ["small", "medium", "large"]:
			for graphKind in ["sparse", "balanced", "dense"]:
				foundValidGraph = False
				while foundValidGraph == False:
					n = random.randint(nList[sizeL.index(sizeType)][0], nList[sizeL.index(sizeType)][1])
					p = random.uniform(pList[graphL.index(graphKind)][0], pList[graphL.index(graphKind)][1])
					(g, source) = generateRandomGraph(n, p)
					buildVertexSet(g)
					buildGraph(g)
					if a(g, source) != False:
						foundValidGraph = True
				print "time to return SSSP using algorithm a on a %s %s graph" % (sizeType, graphKind)
				timeA(g, source)
				print "time to return SSSP using algorithm b on a %s %s graph" % (sizeType, graphKind)
				timeB(g, source)
				print "time to return SSSP using algorithm c on a %s %s graph" % (sizeType, graphKind)
				timeC(g, source)
				print "time to return SSSP using algorithm d on a %s %s graph" % (sizeType, graphKind)
				timeD(g, source)
				print "time to return SSSP using algorithm e on a %s %s graph" % (sizeType, graphKind)
				timeE(g, source)
	else:
		print "unrecognized argument: ", sys.argv[1]

if __name__ == "__main__":
	process(sys.argv)