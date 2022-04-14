import random
import time
from car import Car
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, max_y, min_y):
        self.max_y_cor = max_y
        self.min_y_cor = min_y
        self.level = 1
        self.CARS = []

    def spawn_car(self):
        random_value = random.randint(1, 4)
        if random_value == 1:
            car = Car(random.choice(COLORS), random.randint(self.min_y_cor, self.max_y_cor))
            self.CARS.append(car)

    def move_cars(self):
        for car in self.CARS:
            car.move(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (self.level - 1)))

    def remove_car(self, car):
        self.CARS.remove(car)
        car.ht()
        del car
