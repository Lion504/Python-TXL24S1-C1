class Elevator:
    def __init__ (self, floor_bottom, floor_top):
        self.floor_bottom = floor_bottom
        self.floor_top = floor_top
        self.floor_want_go = 0
        self.current_floor = 1

    def elevator_move(self,floor_get):
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

    def move_up(self):
        for up in range(self.current_floor,self.floor_want_go+1,1):
            print(f"Going up, floor {up} ")
        self.current_floor= self.floor_want_go

    def move_down(self):
        for down in range(self.current_floor,self.floor_want_go-1,-1):
            if down == 0: #skip 0
                continue
            print(f"Going down, floor {down}")

        self.current_floor = self.current_floor

    def initial_elevator(self):
        self.current_floor = 1
        print("initialise elevator to 1 floor")

class Building(Elevator):
    def __init__ (self, floor_bottom, floor_top, elevator_num):
        self.floor_bottom = floor_bottom
        self.floor_top = floor_top
        self.elevator_num = elevator_num
        self.elevator = Elevator(floor_bottom, floor_top)
    def run_elevator(self, accept_floor, accept_elevator):
        print(f"You chosen No.{accept_elevator} elevator.")
        self.elevator.elevator_move(accept_floor)
        


new_building = Building(-3,8,5)

new_building.run_elevator(2,3)

new_building.run_elevator(9,1) #top floor out of range
new_building.run_elevator(-4,4) #bottom floor out of range
new_building.run_elevator(-1,2) #bottom floor out of range negative number test
new_building.run_elevator(2,-1) #elevator out of range negative number test
