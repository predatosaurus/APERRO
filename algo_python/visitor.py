from random import randint
import time


class Visitor:
    def __init__(self, graph):
        self.graph_ = graph
        self.best_drone = None
        self.best_drone_time = None

    

    def visit_drone(self, speed):
        if self.best_drone is None:
            return
        self.graph_.reset()
        time_to_visit = 0
        for link in self.best_drone:
            print("analysing street : ", end="")
            link.show()
            time_to_visit += link.visit(speed)
            #time.sleep(link.visit(speed) // 2)
        print("--------------------------")
        print("you start from point " + self.best_drone[0].get_begin().name_ + " you arrive to point " + self.best_drone[-1].get_end().name_)
        print("the time of operation is " + str(time_to_visit) + "s")
