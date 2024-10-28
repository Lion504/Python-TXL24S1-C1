import random

#for generate cars and car result
class Car:

    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

#create car_num_list and a speed_limit for each car as a list
    @classmethod
    def create_cars(cls):
        cls.car_list = []
        car_nums = [f"ABC-{car_num}" for car_num in range(1, 11)]
        speeds = [random.randint(100, 200) for _ in range(len(car_nums))]
        for i in range(len(car_nums)):
            car = Car(registration_number=car_nums[i], maximum_speed=speeds[i])
            cls.car_list.append(car)
        print(cls.car_list)
        return cls.car_list

#for the result print
    @classmethod
    def race_result(self):
        return (f"{self.registration_number:>13}       |  {self.maximum_speed:>5}km/h    |  {self.current_speed:>5}km/h    | {self.travelled_distance:>9}km")

#for car movement
class Car_run(Car):
    def __init__(self,registration_number,maximum_speed):
        super().__init__(registration_number,maximum_speed)

#car moved by distance
    def drive(self):
        self.travelled_distance += self.current_speed

#car speed changing here
    def accelerate(self):
        car_accelerate = random.randint(-10, 15)
        self.current_speed += car_accelerate
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

#for car run process per hour
class Race():
    def __init__(self, name, distance_limit, joined_car):
        self.name = name
        self.distance_limit = distance_limit
        self.joined_car = joined_car

#status changing per hour
    def hour_pass(self):
        time = 0
        race_end = self.race_finished()
        while not race_end:
            time += 1
            print(f"{time}hours")
            for car in self.joined_car:
                self.name.accelerate()
                self.name.drive()
            self.print_status()
            race_end = self.race_finished()

#get the changing
    def print_status(self):
        for car in self.joined_car:
            print(f" hour's result: {Car.race_result()}")

#finished race here
    def race_finished(self):
        return any(car.travelled_distance >= self.distance_limit for car in self.joined_car)

def main():
    cars = Car.create_cars()
    car_move = Car_run()
    run_race = Race(car_move,10000,cars)
    run_race.hour_pass()

if __name__ == "__main__":
    main()









