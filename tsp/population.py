"""
Population module for the Traveling Salesman Problem.
"""

from typing import List, Optional
from .route import Route
from .city import City

class RoutePop:
    """
    Represents a population of routes in the genetic algorithm.
    
    Attributes:
        rt_pop (List[Route]): List of routes in the population
        size (int): Size of the population
        fittest (Route): The best route in the population
    """
    
    def __init__(self, size: int, cities: List[City], initialise: bool = True):
        """
        Initialize a population of routes.
        
        Args:
            size (int): Size of the population
            cities (List[City]): List of cities to create routes from
            initialise (bool): Whether to initialize the population with random routes
        """
        self.rt_pop: List[Route] = []
        self.size = size
        self.fittest: Optional[Route] = None
        
        # Initialize with empty routes if not initializing with random routes
        if not initialise:
            self.rt_pop = [None] * size
        else:
            for _ in range(size):
                new_rt = Route(cities)
                self.rt_pop.append(new_rt)
            self.get_fittest()

    def get_fittest(self) -> Route:
        """
        Get the fittest (shortest) route in the population.
        
        Returns:
            Route: The best route in the population
        """
        self.rt_pop.sort(key=lambda x: x.length)
        self.fittest = self.rt_pop[0]
        return self.fittest

    def get_route(self, index: int) -> Route:
        """
        Get a route from the population by index.
        
        Args:
            index (int): Index of the route to get
            
        Returns:
            Route: The route at the specified index
        """
        return self.rt_pop[index]

    def save_route(self, index: int, route: Route) -> None:
        """
        Save a route at a specific index in the population.
        
        Args:
            index (int): Index where to save the route
            route (Route): Route to save
        """
        self.rt_pop[index] = route

    def __repr__(self) -> str:
        return f"RoutePop(size={self.size}, fittest_length={self.fittest.length if self.fittest else 'None'})" 