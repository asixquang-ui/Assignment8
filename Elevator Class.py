class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target):
        print(f"Moving to floor {target}...")
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
            
            
            # Test Elevator
elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n🔥 FIRE ALARM! All elevators go to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)
            
            
            # Test Building
building = Building(1, 10, 3)

building.run_elevator(0, 7)
building.run_elevator(1, 5)

building.fire_alarm()


import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance += self.current_speed * hours
        
        
        
        class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        print(f"{'Car':10} {'Speed':10} {'Distance':10}")
        for car in self.cars:
            print(f"{car.reg_number:10} {car.current_speed:<10} {car.distance:<10.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False
    
    
    # Create cars
cars = []
for i in range(10):
    reg = f"ABC-{i+1}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg, max_speed))

# Create race
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

# Final status
print("\n🏁 Race Finished!")
race.print_status()
