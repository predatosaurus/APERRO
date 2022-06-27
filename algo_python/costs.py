import time


class ResourcesManager:
    def __init__(self):
        self.NB_EMPLOYEE = 3000
        self.NB_MACHINES = 2200
        self.PRICE_EMPLOYEE = 20
        self.PRICE_MACHINE = 10

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

    def operation_terminated(self):
        self.free_machine = self.NB_MACHINES
        self.free_employee = self.NB_EMPLOYEE
        print("The operation has been terminated, everyone came back to the warehouse")
        time.sleep(2)

    def get_cost(self, nb_hours):
        res = (self.get_machine_working() * self.PRICE_MACHINE + self.get_personal_working() * self.PRICE_EMPLOYEE) * nb_hours
        print("The cost of this operation is estimated at " + str(res) + "$")
        time.sleep(2)
        return res


def simulation():
    pause = 2
    print("Init situation, all employees and machine are free");
    warehouse = ResourcesManager()
    total_cost = 0

    time.sleep(pause)

    print("few snow start to fall, few machines are deployed principaly to put salt and abrasives on the roads and "
          "sidewalks")
    warehouse.employ(150)
    warehouse.use_machine(100)
    print("the operation is fast and will last 6 hours")

    time.sleep(pause)

    total_cost += warehouse.get_cost(6)
    warehouse.operation_terminated()

    time.sleep(pause)

    print("now more snow fall, we need to remove snow")
    warehouse.employ(750)
    warehouse.use_machine(370)
    print("the operation will last from the night to the morning (12 hours)")
    total_cost += warehouse.get_cost(12)
    warehouse.operation_terminated()

    time.sleep(pause)

    print("in two days the weather will be very snowing, our staff get prepared to act fast in all the city")
    print("we decide to put out the machines in the important places with 2 or 3 workers to continu remove the few "
          "snow that last")
    warehouse.employ(500)
    warehouse.use_machine(150)

    time.sleep(pause)

    total_cost += warehouse.get_cost(48)

    print("the snow day is today we add machines and worker for the rest of the city and the most important streets")
    warehouse.employ(2000)
    warehouse.use_machine(1600)
    print("the maximum alert of snow will last for all the day")

    time.sleep(pause)

    total_cost += warehouse.get_cost(20)
    warehouse.operation_terminated()

    time.sleep(pause)

    print("end of the week, the total costs has been evaluated according to the weather")
    print("The total cost for this week is estimated at " + str(total_cost) + "$")

    time.sleep(pause)

    return total_cost
