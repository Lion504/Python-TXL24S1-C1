class Elevator:
    def __init__ (self, floor_bottom, floor_top):
        self.floor_bottom = floor_bottom
        self.floor_top = floor_top
        self.floor_want_go = 0
        self.current_floor = 1

    def go_to_floor(self,floor_get):
        if floor_get > self.floor_top:
            print("It's too high to reach!")
        elif floor_get < self.floor_bottom:
            print("It's too deep to go bro!")
        else:
            if floor_get > self.current_floor:
                self.floor_want_go = floor_get
                self.floor_up()
                print(f"You are reached {self.floor_want_go} floor")
            elif floor_get < self.current_floor:
                self.floor_want_go = floor_get
                self.floor_down()
                print(f"You are reached {self.floor_want_go} floor")

    def floor_up(self):
        for up in range(self.current_floor,self.floor_want_go+1,1):
            print(f"Going up, floor {up} ")
        self.current_floor= self.floor_want_go

    def floor_down(self):
        for down in range(self.current_floor,self.floor_want_go-1,-1):
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
        self.elevator.go_to_floor(accept_floor+1)
        


new_building = Building(1,8,5)

new_building.run_elevator(2,3)