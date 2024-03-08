import numpy as np


class Particle:
    def __init__(self, id, position, rotation, num_magnets, magnets, neighborhood):
        self.id = id
        self.position = position
        self.rotation = rotation
        self.num_magnets = num_magnets
        self.magnets = magnets
        self.neighborhood = neighborhood

    def changeMagnet(self, magnet_number: int, polarity: int, intensity: float):
        self.magnets[magnet_number] = (polarity, intensity)


