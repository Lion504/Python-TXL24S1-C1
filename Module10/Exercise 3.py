class Elevator:
    def __init__(self, floor_bottom, floor_top):
        self.floor_bottom = floor_bottom
        self.floor_top = floor_top
        self.floor_want_go = 0
        self.current_floor = 1

    def elevator_move(self, floor_get):
        if floor_get > self.floor_top:
            print(f"Sorry {floor_get} floor is too high to reach!")
        elif floor_get < self.floor_bottom:
            print(f"Sorry {floor_get} floor too deep to go bro!")
        else:
            if floor_get > self.current_floor:
                self.floor_want_go = floor_get
                self.move_up()
                print(f"You are reached {self.floor_want_go} floor")
            elif floor_get < self.current_floor:
                self.floor_want_go = floor_get
                self.move_down()
                print(f"You are reached {self.floor_want_go} floor")
            else:
                print(f"You are already at {self.current_floor} floor")

    def move_up(self):
        for up in range(self.current_floor, self.floor_want_go + 1, 1):
            print(f"Going up, floor {up} ")
        self.current_floor = self.floor_want_go

    def move_down(self):
        for down in range(self.current_floor, self.floor_want_go - 1, -1):
            if down == 0:  #skip 0
                continue
            print(f"Going down, floor {down}")

        self.current_floor = self.floor_want_go

class Building:
    def __init__(self, floor_bottom, floor_top, elevator_num):
        self.floor_bottom = floor_bottom
        self.floor_top = floor_top
        self.elevator_num = elevator_num
        self.elevators = [Elevator(floor_bottom, floor_top) for _ in range(elevator_num)]# create several class for each elevator
    def run_elevator(self, accept_floor, accept_elevator):
        if accept_elevator > self.elevator_num:
            print(f"No.{accept_elevator} elevator not exist!")
            return
        elif accept_elevator <= 0:
            print(f"No.{accept_elevator} elevator not exist!")
            return

        elevator = self.elevators[accept_elevator - 1]
        print(f"start from {accept_elevator} elevator move from {elevator.current_floor}")

        elevator.elevator_move(accept_floor)

    def fire_alarm(self):
        i = 4
        for elevator in self.elevators:
            elevator.current_floor = 1
            print(f"initialise {len(self.elevators)-i} elevator to 1 floor")
            i -= 1

new_building = Building(-3, 8, 5)

new_building.run_elevator(2, 3)

new_building.fire_alarm()

'''#test
new_building.run_elevator(5, 1)
new_building.run_elevator(2, 1)
new_building.run_elevator(4, 3)
new_building.run_elevator(2, 1)
new_building.run_elevator(3, 1)  #top floor out of range
new_building.run_elevator(-4, 4)  #bottom floor out of range
new_building.run_elevator(-1, 2)  #bottom floor out of range negative number test
new_building.run_elevator(5, 5)  #bottom floor out of range negative number test

new_building.run_elevator(2, -1)  #elevator out of range negative number test'''
