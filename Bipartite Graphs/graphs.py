from random import random
from random import shuffle

class graph:

	""" The vertices variable must be a set. The edges variable must be a set of pair tuples of elements in the vertices variable. """
	def __init__(self, vertices, edges, type = "not specified", skipCheck = False):
		if not skipCheck:
			if not isinstance(vertices, set):
				raise ValueError("vertices must be a set")
			if not isinstance(edges, set):
				raise ValueError("edges must be a set")

			for edge in edges:
				if not isinstance(edge, tuple):
					raise ValueError("each edge must be a tuples")
				if len(edge) != 2:
					raise ValueError("each edge must be between two vertices")
				if edge[0] not in vertices or edge[1] not in vertices:
					raise ValueError("each edge must be between two vertices")
				if ((edge[1], edge[0]) in edges) and (edge[0] != edge[1]):
					raise ValueError("this class excludes multigraphs and digraphs")
		
		# else:
		self.V = vertices
		self.E = edges
		self.type = type

	
	"""Some special initialization functions: """

	def clique(num):
		vertices = {i for i in range(num)}
		edges = {(i, j) for i in range(num) for j in range(i + 1, num)}

		return graph(vertices, edges, "clique", True)

	def randGraph(num, p):
		vertices = {i for i in range(num)}

		preEdges = [(i, j, random()) for i in range(num) for j in range(i + 1, num)]

		Edges = set()
		for edge in preEdges:
			if edge[2] < p: Edges.add((edge[0], edge[1]))

		return graph(vertices, Edges, "random", True)

	def completeBipartite(num1, num2):
		partA = {i for i in range(num1)}
		partB = {i for i in range(num1, num1 + num2)}

		edges = {(i, j) for i in partA for j in partB}

		return graph(partA | partB, edges, "complete bipartite", True)

	def randBipartite(num1, num2, p):
		partA = {i for i in range(num1)}
		partB = {i for i in range(num1, num1 + num2)}

		preEdges = [(i, j, random()) for i in partA for j in partB]

		Edges = set()
		for edge in preEdges:
			if edge[2] < p: Edges.add((edge[0], edge[1]))

		return graph(partA | partB, Edges, "random bipartite", True)

	"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


# Goal: Check if a graph is bipartite or not:

def areNeighbors(graph, v1, v2):
	return (v1, v2) in graph.E or (v2, v1) in graph.E

def getNeighborhood(graph, v1):
	return {v for v in graph.V if (v1, v) in graph.E or (v, v1) in graph.E}

# def makeBFSTree(graph, v1):
# 	bank = graph.V - {v1}
# 	treeBank = getNeighborhood(graph, v1) - {v1}

# 	treeVertices = {v1}
# 	treeEdges = set()
# 	while len(treeBank) != 0:
# 		v = treeBank.pop()





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #	
# Tests:
K = graph.clique(5)
G = graph.randGraph(5, 0.5)
B = graph.completeBipartite(4, 3)
BG = graph.randBipartite(3, 4, 0.5)

print(BG.E)
print(B.E)


print(areNeighbors(B, 1, 4))
print(areNeighbors(B, 1, 2))

print(getNeighborhood(BG, 0))

print(len(BG.V))

