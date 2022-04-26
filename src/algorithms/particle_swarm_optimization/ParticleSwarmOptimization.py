from typing import Callable, List
from .Particle import Particle

class ParticleSwarmOptimization():
    def __init__(
        self,
        function_: Callable,
        boundaries: List[List[float]],
        number_iteration: int,
        number_particle: int,
        exploration_acceleration: float =1.05,
        exploitation_acceleration: float = 1.4
    ):
        self.function_ = function_
        self.boundaries = boundaries
        self.number_iteration = number_iteration
        self.particles = [
            Particle(
                function_,
                boundaries,
                exploration_acceleration,
                exploitation_acceleration,
            ) for _ in range(number_particle)
        ]
        
        self.position = self.particles[0].position
        self.best_fitness = self.particles[0].best_fitness
        self.best_fitness_set = []
    
    def optimize(self):
        for iteration_index in range(self.number_iteration):
            for particle_index in range(len(self.particles)):                
                if self.particles[particle_index].best_fitness < self.best_fitness:
                    self.position = self.particles[particle_index].position # g_best position
                    self.best_fitness = self.particles[particle_index].best_fitness
            
            for particle_index in range(len(self.particles)):
                self.particles[particle_index].update(0.1 / (iteration_index + 1), self.position)
                
            self.best_fitness_set.append(self.best_fitness)