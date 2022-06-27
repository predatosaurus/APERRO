from graph_object import Graph, Node

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
K = Node("K")
L = Node("L")
M = Node("M")
N = Node("N")


links_start = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 10, 12, 12, 13, 13]
links_end = [1, 6, 2, 7, 3, 8, 4, 5, 10, 6, 12, 8, 9, 13, 10, 13, 11, 7, 11, 12, 11]
distances = [12, 6, 13, 4, 10, 4, 8, 15, 6, 6, 5, 3, 3, 1, 2, 2, 3, 2, 1, 2, 1]
two_ways = [True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, False, False, False, False]

nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N]

MyGraph = Graph()
MyGraph.add_nodes(nodes)

for i in range(len(links_start)):
    MyGraph.link_nodes(links_start[i], links_end[i], distances[i], two_way=two_ways[i])
