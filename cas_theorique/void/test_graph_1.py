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

links_start = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6, 8]
links_end = [1, 6, 7, 8, 2, 6, 3, 4, 5, 6, 4, 9, 9, 6, 8, 7, 9]
distances = [3, 2, 1, 4, 5, 1, 5, 3, 3, 4, 2, 9, 3, 2, 5, 1, 4]

nodes = [A, B, C, D, E, F, G, H, I, J]

MyGraph = Graph()
MyGraph.add_nodes(nodes)

for i in range(len(links_start)):
    MyGraph.link_nodes(links_start[i], links_end[i], distances[i])
