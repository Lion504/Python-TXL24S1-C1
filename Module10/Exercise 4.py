import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


class Car_run(Car):
    def __init__(self, registration_number, maximum_speed):
        super().__init__(registration_number, maximum_speed)

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


def create_car():
    name = [f"ABC-{car_num}" for car_num in range(1, 11)]
    speeds = [random.randint(100, 200) for _ in range(len(name))]
    car_list = []

    for i in range(len(name)):
        car = Car_run(registration_number=name[i], maximum_speed=speeds[i])
        car_list.append(car)
    return car_list


class Race:
    def __init__(self, name, distance, joined_car):
        self.name = name
        self.distance_limit = distance
        self.joined_car = joined_car

    def hour_passes(self):
        for car in self.joined_car:
            car.accelerate()
            car.drive()

    def print_status(self):

        print(f"Racing Name: {self.name}\nDistance:{self.distance_limit}")
        print(f"{'Registration number'} | {'Maximum speed':} | {'Current Speed'} | {'Travelled_distance'}")
        print("")

        for car in self.joined_car:
            print(
                f"{car.registration_number:>13}       |  {car.maximum_speed:>5}km/h    |  {car.current_speed:>5}km/h    | {car.travelled_distance:>9}km")
        print("-" * 80)

    def race_finished(self):
        return any(car.travelled_distance >= self.distance_limit for car in self.joined_car)


def main():
    race_distance = 8000
    race_name = "Grand Demolition Derby"
    cars = create_car()
    race = Race(race_name, race_distance, cars)

    time = 0
    while not race.race_finished():
        time += 1
        race.hour_passes()
        if time % 10 == 0:
            print(f"{time}hours")
            race.print_status()

    print(f"Race finished in {time} hours")
    race.print_status()



if __name__ == "__main__":
    main()
