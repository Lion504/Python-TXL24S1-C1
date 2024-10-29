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
        for car in self.joined_car:
            car.accelerate()
            car.drive()

    def print_status(self):

        print(f"{self.name},{self.distance_limit}")
        print(f"{'Registration number'} | {'Maximum speed':} | {'Current Speed'} | {'Travelled_distance'}")
        print("")
        for car in self.joined_car:
            print(f"{car.registration_number:>13}       |  {car.maximum_speed:>5}km/h    |  {car.current_speed:>5}km/h    | {car.travelled_distance:>9}km")
        print("-" * 80)

def main():
    race_distance = 8000
    race_name = "Grand Demolition Derby"
    cars = []
    e_car = Electric_Car("ABC-15", 180, 52.5)
    print(f"Car Type 1: Electric Car\nRegistration Number:{e_car.registration_number}  |  Maximum Speed:{e_car.maximum_speed}km/h  |  Battery Capacity:{e_car.battery}Kwh")
    car = Car_run(e_car.registration_number,e_car.maximum_speed)
    cars.append(car)

    g_car = Gasoline_Car("ACD-123", 165, 32.3)
    print(f"Car Type 2: Gasoline Car\nRegistration Number:{g_car.registration_number}  |  Maximum Speed:{g_car.maximum_speed}km/h  |  Battery Capacity:{g_car.gas_volume}L")
    car = Car_run(g_car.registration_number,g_car.maximum_speed)
    cars.append(car)

    race = Race(race_name,race_distance,cars)
    print(f"\n{'*'*30}Test Race begin{'*'*30}")

    time = 0
    while time<= 3:
        time += 1
        race.hour_passes()
        print(f"{time}hours")
        race.print_status()

    print(f"Race finished in {time} hours")

if __name__ == "__main__":
    main()
