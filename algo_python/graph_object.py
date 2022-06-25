from enum import Enum


class SnowLevel(Enum):
    AUCUN = 0
    EPANDAGE = 2.5
    DEBLAIEMENT = 15
    CHARGEMENT = 30
    TEMPETE = 40


class ResourcesManager:
    def __init__(self):
        self.NB_EMPLOYEE = 3000
        self.NB_MACHINES = 2200

        if self.NB_EMPLOYEE < self.NB_MACHINES:
            self.NB_EMPLOYEE = self.NB_MACHINES

        self.free_employee = self.NB_EMPLOYEE
        self.free_machine = self.NB_MACHINES

    def get_personal_working(self):
        return self.NB_EMPLOYEE - self.free_employee

    def get_machine_working(self):
        return self.NB_MACHINES - self.free_machine

    def employ(self, request=1):
        if self.free_employee >= request > 0:
            self.free_employee -= request

    def unemploy(self, request=1):
        if self.free_employee + request <= self.NB_EMPLOYEE and request > 0:
            self.free_employee += request
            while self.get_machine_working() > self.get_personal_working():
                self.unuse_machine()

    def use_machine(self, request=1):
        if self.free_machine >= request > 0:
            self.free_machine -= request
            while self.get_machine_working() > self.get_personal_working():
                self.employ()

    def unuse_machine(self, request=1):
        if self.free_machine + request <= self.NB_MACHINES and request > 0:
            self.free_machine += request


class Link:
    def __init__(self, node_start, node_end, distance, important=False, snow_level=None, two_way=True):
        self.node_start_ = node_start
        self.node_end_ = node_end
        self.distance_ = distance

        self.important_ = important
        self.snow_level_ = snow_level

        self.two_way_ = two_way

        self.visited = False

    def is_important(self):
        return self.important_

    def get_snow_level(self):
        return self.snow_level_

    def remove_snow(self):
        self.snow_level_ = SnowLevel.AUCUN

    def set_snow_level(self, snow_level):
        self.snow_level_ = snow_level

    def reset(self):
        self.visited = False

    def visit(self, speed=1, rec=True):
        self.visited = True
        if speed <= 0:
            speed = 1
        if self.two_way_ and rec:
            self.get_end().get_link_opposite(self.get_begin()).visit(speed, False)
        return self.distance_ / speed  # get time to visit de street

    def is_visited(self):
        return self.visited

    def get_begin(self):
        return self.node_start_

    def get_end(self):
        return self.node_end_

    def link_opposite(self):
        if self.two_way_:
            opposite_link = Link(self.get_end(), self.get_begin(), self.distance_, self.important_, self.snow_level_, True)
            self.get_end().add_link(opposite_link)

    def show(self):
        print(self.get_begin().name_ + " ---> " + self.get_end().name_)


class Node:
    def __init__(self, name, links=None):
        self.name_ = name
        if links is None:
            self.links_ = []
        else:
            self.links_ = links
        self.nb_links_ = len(self.links_)

    def is_pair(self):
        return self.nb_links_ % 2 == 0

    def add_link(self, link):
        self.links_.append(link)
        self.nb_links_ += 1

    def add_links(self, links):
        for link in links:
            self.add_link(link)

    def get_links(self):
        if self.nb_links_ == 0:
            return None
        return self.links_

    def get_links_to_visit(self):
        res = []
        if self.get_links() is not None:
            for link in self.get_links():
                if link.is_visited() is False:
                    res.append(link)
        if len(res) == 0:
            res = None
        return res

    def reset(self):
        if self.get_links() is not None:
            for link in self.get_links():
                link.reset()

    def get_link_opposite(self, node):
        res = None
        if self.get_links() is not None:
            for link in self.get_links():
                if link.get_end() == node:
                    res = link
        return res


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes_ = []
        else:
            self.nodes_ = nodes
        self.nb_nodes_ = len(self.nodes_)
        self.nb_links_ = self.count_links()

    def list_starting_points(self):
        res = []
        for node in self.nodes_:
            if node.is_pair():
                res.append(node)
        if len(res) == 0:
            res = None
        return res

    def get_nodes(self):
        return self.nodes_

    def get_nb_nodes(self):
        return self.nb_nodes_

    def count_links(self):
        res = 0
        for node in self.nodes_:
            if node.get_links() is not None:
                for link in node.get_links():
                    if link.is_visited() is False:
                        res += 1
                        link.visit()
        return res

    def reset(self):
        for node in self.nodes_:
            node.reset()

    def add_node(self, node):
        self.nodes_.append(node)
        self.nb_nodes_ += 1

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def link_nodes(self, a, b, distance, important=False, snow_level=None, two_way=True):
        if a < self.nb_nodes_ and b < self.nb_nodes_:
            new_link = Link(self.nodes_[a], self.nodes_[b], distance, important, snow_level, two_way)
            self.nodes_[a].add_link(new_link)
            if two_way:
                new_link.link_opposite()
            self.nb_links_ += 1

    def fully_visited(self):
        for node in self.nodes_:
            if node.get_links() is not None:
                for link in node.get_links():
                    if link.is_visited() is False:
                        return False
        return True

    def show(self):
        for node in self.nodes_:
            for link in node.get_links():
                print(node.name_ + " ---> " + link.get_end().name_ + " (distance = " + str(link.distance_) + ")")
