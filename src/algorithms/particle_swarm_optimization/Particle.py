from random import random, uniform
from typing import Callable, List

class Particle:
    def __init__(
        self,
        function_: Callable,
        boundaries: List[List[float]],
        exploration_acceleration: float = 1,
        exploitation_acceleration: float = 1
    ):
        self.function_ = function_
        self.boundaries = boundaries
        self.exploration_acceleration = exploration_acceleration
        self.exploitation_acceleration = exploitation_acceleration

        self.position = []
        self.velocity = []
        for dimension_index in range(len(boundaries)):
            self.position.append(
                uniform(
                    boundaries[dimension_index][0],
                    boundaries[dimension_index][1]
                )
            )
            self.velocity.append(0.01)
        
        self.best_position = self.position
        self.best_fitness = function_(self.position)


    def _update_the_best(self):
        fitness = self.function_(self.position)
        if fitness < self.best_fitness:
            self.best_position = self.position
            self.best_fitness = fitness


    def update(self, k: float, group_position: float):
        max_velocity = (k * (max(self.boundaries[1]) - min(self.boundaries[0]))) / 2

        for index in range(len(self.position)):
            exploration = \
                random() \
                * self.exploration_acceleration \
                * (self.best_position[index] - self.position[index])
            
            exploitation = \
                random() \
                * self.exploitation_acceleration \
                * (group_position[index] - self.position[index])
            
            self.velocity[index] = \
                self.velocity[index] \
                + exploration \
                + exploitation
            
            if self.velocity[index] > max_velocity:
                self.velocity[index] = max_velocity
            elif self.velocity[index] < -max_velocity:
                self.velocity[index] = -max_velocity

            self.position[index] += self.velocity[index]
            
            if self.position[index] < self.boundaries[index][0]:
                self.position[index] = self.boundaries[index][0]

            elif self.position[index] > self.boundaries[index][1]:
                self.position[index] = self.boundaries[index][1]

        self._update_the_best()