import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def race_result(self):
        return (f"registration number: ABC-{self.registration_number:>10} | "
                f"maximum speed: {self.maximum_speed:>12} km/h | "
                f"current speed: {self.current_speed:>12} km/h | "
                f"travelled distance: {self.travelled_distance:>12} km")


class Car_run(Car):
    def __init__(self, registration_number, maximum_speed):
        super().__init__(registration_number, maximum_speed)

    def drive(self):
        # Add the current speed to travelled distance for this hour
        self.travelled_distance += self.current_speed

    def accelerate(self):
        # Change speed randomly between -10 and +15 km/h
        car_accelerate = random.randint(-10, 15)
        self.current_speed += car_accelerate

        # Ensure the current speed is within bounds
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0


def create_cars():
    car_nums = [f"ABC-{car_num}" for car_num in range(1, 11)]
    speeds = [random.randint(100, 200) for _ in range(len(car_nums))]
    car_list = []
    for i in range(len(car_nums)):
        # Create cars as Car_run objects
        car = Car_run(registration_number=car_nums[i], maximum_speed=speeds[i])
        car_list.append(car)
    return car_list


def car_race(cars):
    time = 0
    race_end = False

    while not race_end:
        time += 1
        print(f"Hour {time}:")

        for car in cars:
            car.accelerate()  # Accelerate the car
            car.drive()  # Drive the car for 1 hour

            # Check if any car has reached or exceeded 10,000 km
            if car.travelled_distance >= 10000:
                race_end = True
                print(f"\nCar {car.registration_number} has reached 10,000 km! Race over!")
                break

        # Show the race results after each hour
        show_result(cars)


def show_result(result):
    print("-" * 80)
    for car in result:
        print(car.race_result())
    print("-" * 80)


# Create the list of cars
all_cars = create_cars()

# Start the race
car_race(all_cars)
