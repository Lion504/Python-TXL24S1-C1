class Car:
    def __init__(self,registration_number,maximum_speed,current_speed=0,travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    def new_car(self):
        return f"The new car: \nregistration number: {self.registration_number}\nmaximum speed: {self.maximum_speed}km/h\ncurrent speed: {self.current_speed}km/h\ntravelled distance: {self.travelled_distance}km"


print_new_car = Car("ABC-123",142)
print(print_new_car.new_car())
