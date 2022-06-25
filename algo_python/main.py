from test_graph_2 import MyGraph
from visitor import Visitor

if __name__ == '__main__':
    v = Visitor(MyGraph)
    v.find_best_parcours(100000)
    v.visit_drone(3)