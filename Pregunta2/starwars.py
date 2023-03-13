""" Aca esta la segunda pregunta de la prueba tecnica de Data Observatory """
from __future__ import annotations
import math
import json


class Person:
    """Class describing a person in the Star Wars Universe"""
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
        self.homeworld: object = homeworld
        self.__species: str = species
        self.__vehicles: list = vehicles
        self.__starships: list = starships
        self.url: str = url

    def calculate_imc(self) -> float:
        """Function to calculate the IMC of a given person"""
        return self.__mass/(self.height**2)

    def is_human(self) -> bool:
        """Function to know if a person is human or not"""
        if "human" in self.__species:
            return True
        return False

    def total_vehicles_and_ships(self) -> int:
        """Gets the sum of vehicles and ships that the person owns"""
        return self.__vehicles.count() + self.__starships.count()

    def who_is_older(self, against: Person) -> Person:
        """Given another person, return who is older"""
        against_birth_year = against.get_birthyear()
        if self.__birth_year.endswith("BBY"):
            if against_birth_year.endswith("ABY"):
                return self
            else:
                birth_self = int(self.__birth_year[:-3])
                birth_against = int(against_birth_year[:-3])
                if birth_self > birth_against:
                    return self
                else:
                    return against
        elif self.__birth_year.endswith("ABY"):
            if against_birth_year.endswith("BBY"):
                return against
            else:
                birth_self = int(self.__birth_year[:-3])
                birth_against = int(against_birth_year[:-3])
                if birth_self > birth_against:
                    return self
                else:
                    return against

    def get_birthyear(self) -> str:
        """Return the birthyear of the person"""
        return self.__birth_year

    def get_homeworld(self) -> object:
        """Return the homeworld of the person as an object"""
        return self.homeworld


class Planet:
    """Class describing a planet in the Star Wars Universe"""
    def __init__(  # pylint: disable=too-many-arguments
        self, name, rotation_period, orbital_period, diameter,
        climate, gravity, terrain, surface_water, population
    ) -> None:
        self.name: str = name
        self.rotation_period: int = rotation_period
        self.orbital_period: int = orbital_period
        self.__diameter: int = diameter
        self.climate: str = climate
        self.gravity: str = gravity
        self.terrain: list = terrain
        self.__surface_water: int = surface_water
        self.__population: int = population

    def get_surface_in_km_squared(self) -> float:
        """Returns the surface of the planet in km^2"""
        return math.pi*(self.__diameter**2)

    def get_poblational_density(self) -> float:
        """Returns the population density in people/km^2"""
        return self.__population / self.get_surface_in_km_squared()

    def get_water_covered_surface_in_km_squared(self) -> float:
        """Returns the amount of surface covered in water in km^2"""
        return self.__surface_water * self.get_surface_in_km_squared

    def get_km_sq_of_water_per_habitant(self) -> float:
        """Returns the amount of water per habitant in km^2"""
        return self.get_water_covered_surface_in_km_squared / self.__population
