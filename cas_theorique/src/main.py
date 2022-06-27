from graph import Graph

if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    pairs = [('A', 'B', 3),
            ('B', 'A', 3),
            ('B', 'D', 1),
            ('D', 'B', 4),
            ('B', 'F', 5),
            ('F', 'B', 5),
            ('C', 'A', 8),
            ('A', 'E', 6),
            ('E', 'C', 8)]
    g = Graph(nodes, pairs, directed=True)
    print(g.find_eulerian_cycle())
    g.plot()
