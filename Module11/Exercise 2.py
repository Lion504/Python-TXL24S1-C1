import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

class Electric_Car(Car):
    def __init__(self,registration_number,maximum_speed,battery):
        super().__init__(registration_number,maximum_speed)
        self.battery = battery

class Gasoline_Car(Car):
    def __init__(self,registration_number,maximum_speed,gas_volume):
        super().__init__(registration_number,maximum_speed)
        self.gas_volume = gas_volume

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

class Race:
    def __init__(self, name, distance, joined_car):
        self.name = name
        self.distance_limit = distance
        self.joined_car = joined_car

    def hour_passes(self):
        self.joined_car.accelerate()
        self.joined_car.drive()

    def print_status(self):

        print(f"{self.name},{self.distance_limit}")
        print(f"{'Registration number'} | {'Maximum speed':} | {'Current Speed'} | {'Travelled_distance'}")
        print("")
        print(f"{self.joined_car.registration_number:>13}       |  {self.joined_car.maximum_speed:>5}km/h    |  {self.joined_car.current_speed:>5}km/h    | {self.joined_car.travelled_distance:>9}km")
        print("-" * 80)

def main():
    race_distance = 8000
    race_name = "Grand Demolition Derby"
    e_car = Electric_Car("ABC-15", 180, 52.5)
    car = Car_run(e_car.registration_number,e_car.maximum_speed)
    race_e = Race(race_name, race_distance, car)

    g_car = Gasoline_Car("ACD-123", 165, 32.3)
    car = Car_run(g_car.registration_number,g_car.maximum_speed)
    race_g = Race(race_name, race_distance, car)

    time = 0
    while time<= 3:
        time += 1
        race_e.hour_passes()
        race_g.hour_passes()
        race_e.print_status()
        race_g.print_status()
    print(f"{time}hours")
    race_e.print_status()
    race_g.print_status()

    print(f"Race finished in {time} hours")

if __name__ == "__main__":
    main()
