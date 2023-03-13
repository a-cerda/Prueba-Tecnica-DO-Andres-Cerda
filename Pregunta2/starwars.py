""" Aca esta la segunda pregunta de la prueba tecnica de Data Observatory """
from __future__ import annotations
import json


class Person:
    def __init__(  # pylint: disable=too-many-arguments
        self, name, height, mass, hair_color,
        skin_color, eye_color, birth_year,
        gender, homeworld, species, vehicles, starships, url
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.__mass: int = mass
        self.__hair_color: str = hair_color
        self.__skin_color: str = skin_color
        self.__eye_color: str = eye_color
        self.__birth_year: str = birth_year
        self.gender: str = gender
        self.homeworld: str = homeworld
        self.__species: str = species
        self.__vehicles: list = vehicles
        self.__starships: list = starships
        self.url: str = url

    def calculate_imc(self) -> float:
        return self.__mass/(self.height**2)

    def is_human(self) -> bool:
        if "human" in self.__species:
            return True
        return False

    def total_vehicles_and_ships(self) -> int:
        return self.__vehicles.count() + self.__starships.count()

    def who_is_older(self, against: Person) -> Person:
        pass

    def get_homeworld(self) -> object:
        return self.homeworld

class Planet:
    def __init__( # pylint: disable=too-many-arguments
        self, name, rotation_period, orbital_period, diameter,
        climate, gravity, terrain, surface_water, population
        ) -> None:
        self.name = name
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.__diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.__surface_water = surface_water
        self.__population = population

    def get_surface_in_km_squared(self) -> float:
        pass

    def get_poblational_density(self) -> float:
        pass

    def get_water_covered_surface_in_km_squared(self) -> float:
        pass

    def get_km_sq_of_water_per_habitant(self) -> float:
        pass