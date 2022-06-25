from test_graph_1 import MyGraph
from visitor import Visitor

if __name__ == '__main__':
    v = Visitor(MyGraph)
    v.visit_drone(1)