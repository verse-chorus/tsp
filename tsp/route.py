"""
Route module for the Traveling Salesman Problem.
"""

import random
from typing import List, Callable, TypeVar, Any
from .city import City

T = TypeVar('T')

class Route:
    """
    Represents a route (tour) in the Traveling Salesman Problem.
    
    Attributes:
        route (List[City]): Ordered list of cities in the route
        length (float): Total length of the route
    """
    
    def __init__(self, cities: List[City]):
        """
        Initialize a Route object with a random permutation of cities.
        
        Args:
            cities (List[City]): List of cities to include in the route
        """
        self.route = random.sample(cities, len(cities))
        self.recalc_rt_len()

    def recalc_rt_len(self) -> None:
        """
        Recalculate the total length of the route.
        """
        self.length = 0.0
        for i, city in enumerate(self.route):
            next_city = self.route[(i + 1) % len(self.route)]
            dist_to_next = city.distance_to[next_city.name]
            self.length += dist_to_next

    def pr_cits_in_rt(self, print_route: bool = False) -> str:
        """
        Get a string representation of the cities in the route.
        
        Args:
            print_route (bool): Whether to print the route to console
            
        Returns:
            str: String representation of the route
        """
        cities_str = ', '.join(city.name for city in self.route)
        if print_route:
            print(cities_str)
        return cities_str

    def is_valid_route(self, all_cities: List[City]) -> bool:
        """
        Check if the route is valid (contains all cities exactly once).
        
        Args:
            all_cities (List[City]): List of all cities that should be in the route
            
        Returns:
            bool: True if route is valid, False otherwise
        """
        route_cities = set(city.name for city in self.route)
        all_city_names = set(city.name for city in all_cities)
        return route_cities == all_city_names and len(route_cities) == len(self.route)

    @staticmethod
    def count_mult(seq: List[T], pred: Callable[[T], bool]) -> int:
        """
        Count the number of elements in a sequence that satisfy a predicate.
        
        Args:
            seq (List[T]): Sequence to count in
            pred (Callable[[T], bool]): Predicate function
            
        Returns:
            int: Number of elements satisfying the predicate
        """
        return sum(1 for v in seq if pred(v))

    def __repr__(self) -> str:
        return f"Route(length={self.length:.2f}, cities={self.pr_cits_in_rt()})" 