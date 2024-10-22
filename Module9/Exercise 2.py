from numpy.ma.core import maximum


class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def new_car(self):
        return f"The new car: \nregistration number: {self.registration_number}\nmaximum speed: {self.maximum_speed}km/h\ncurrent speed: {self.current_speed}km/h\ntravelled distance: {self.travelled_distance}km"

class Car_fast(Car):
    def __init__(self,registration_number,maximum_speed):
        super().__init__(registration_number,maximum_speed)
    def accelerate(self, speed_change):
        for s in speed_change:
            self.current_speed += s

            if self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            elif self.current_speed < 0:
                self.current_speed = 0

        return self.current_speed

print_new_car = Car_fast("ABC-123",142)
print_new_car.accelerate([30, 70, 50])
print(print_new_car.new_car())
print_new_car.accelerate([-200])
print(print_new_car.new_car())