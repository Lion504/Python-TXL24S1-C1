import random

class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def race_result(self):
        return (f"{self.registration_number:>13}       |  {self.maximum_speed:>5}km/h    |  {self.current_speed:>5}km/h    | {self.travelled_distance:>9}km")

class Car_run(Car):
    def __init__(self,registration_number,maximum_speed):
        super().__init__(registration_number,maximum_speed)

    def drive(self):
        self.travelled_distance += self.current_speed

    def accelerate(self):
        car_accelerate = random.randint(-10, 15)
        self.current_speed += car_accelerate
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

def create_cars():
    car_nums = [f"ABC-{car_num}" for car_num in range(1, 11)]
    speeds = [random.randint(100, 200) for _ in range(len(car_nums))]
    car_list = []
    for i in range(len(car_nums)):
        car = Car_run(registration_number=car_nums[i],maximum_speed=speeds[i])
        car_list.append(car)
    return car_list

def car_race(cars):
    time = 0
    race_end = False
    while not race_end:
        time += 1
        print(f"{time}hours")
        for car in cars:
            car.accelerate()
            car.drive()
            if car.travelled_distance >=10000:
                race_end = True
                break
        show_result(cars)

def show_result(result):
    print(f"{'Registration number'} | {'Maximum speed':} | {'Current Speed'} | {'Travelled_distance'}")
    print("-")
    for car in result:
        print(car.race_result())
    print("-")
all_cars = create_cars()
car_race(all_cars)








