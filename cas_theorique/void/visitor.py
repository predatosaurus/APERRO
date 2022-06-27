from random import randint
import time


class Visitor:
    def __init__(self, graph):
        self.graph_ = graph
        self.best_drone = None
        self.best_drone_time = None

    def parcours(self, drone=False):
        speed = 1
        time_to_visit = 0
        path = []
        self.graph_.reset()
        starting_node = self.graph_.list_starting_points()
        if starting_node is None:
            starting_node = self.graph_.get_nodes()[randint(0, self.graph_.get_nb_nodes() - 1)]
        else:
            starting_node = starting_node[randint(0, len(starting_node) - 1)]
        current_node = starting_node
        while self.graph_.fully_visited() is False:
            next_links = current_node.get_links_to_visit()
            if next_links is None:
                next_links = current_node.get_links()
                if next_links is None:
                    print("error graph isolated node !")
                    return None, None
            next_link = next_links[randint(0, len(next_links) - 1)]
            if drone is False and next_link.two_way_ is True and next_link.is_visited() is False:
                time_to_visit += next_link.visit(speed)
            time_to_visit += next_link.visit(speed)
            current_node = next_link.get_end()
            path.append(next_link)
        while current_node != starting_node:  # way back to original point
            next_links = current_node.get_links()
            next_link = None
            for i in next_links:
                if i.get_end() == starting_node:
                    next_link = i
            if next_link is None:
                next_link = next_links[randint(0, len(next_links) - 1)]
            path.append(next_link)
            time_to_visit += next_link.visit(speed)
            current_node = next_link.get_end()
        return time_to_visit, path

    def find_best_parcours(self, nb_attemps, drone=False):
        for i in range(nb_attemps):
            t, p = self.parcours(drone)
            if self.best_drone_time is None or t < self.best_drone_time:
                self.best_drone_time = t
                self.best_drone = p

    def visit_drone(self, speed):
        if self.best_drone is None:
            return
        self.graph_.reset()
        time_to_visit = 0
        for link in self.best_drone:
            print("analysing street : ", end="")
            link.show()
            time_to_visit += link.visit(speed)
            # time.sleep(link.visit(speed))
        print("--------------------------")
        print("you start from point " + self.best_drone[0].get_begin().name_ + " you arrive to point " + self.best_drone[-1].get_end().name_)
        print("the time of operation is " + str(time_to_visit) + "s")
