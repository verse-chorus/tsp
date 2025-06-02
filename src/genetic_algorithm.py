"""
Genetic Algorithm implementation for the Traveling Salesman Problem.
"""

import random
from typing import List, Tuple
from .city import City
from .route import Route
from .population import RoutePop

class GeneticAlgorithm:
    """
    Genetic Algorithm implementation for solving the Traveling Salesman Problem.
    
    Attributes:
        mutation_probability (float): Probability of mutation
        tournament_size (int): Size of tournament selection
        elitism (bool): Whether to use elitism
    """
    
    def __init__(self, population_size: int, mutation_probability: float,
                 tournament_size: int, elitism: bool = True):
        """
        Initialize the genetic algorithm.
        
        Args:
            population_size (int): Size of the population
            mutation_probability (float): Probability of mutation
            tournament_size (int): Size of tournament selection
            elitism (bool): Whether to use elitism
        """
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.tournament_size = tournament_size
        self.elitism = elitism

    def run(self, cities: List[City], generations: int) -> Route:
        """
        Run the genetic algorithm.
        
        Args:
            cities (List[City]): List of cities to visit
            generations (int): Number of generations to run
            
        Returns:
            Route: The best route found
        """
        # Initialize population
        pop = RoutePop(self.population_size, cities)
        
        # Calculate initial distances
        for city in cities:
            city.calculate_distances(cities)
        
        # Evolve population
        for _ in range(generations):
            pop = self.evolve_population(pop, cities)
        
        return pop.get_fittest()

    def evolve_population(self, pop: RoutePop, cities: List[City]) -> RoutePop:
        """
        Evolve the population for one generation.
        
        Args:
            pop (RoutePop): Current population
            cities (List[City]): List of cities
            
        Returns:
            RoutePop: Evolved population
        """
        new_population = RoutePop(pop.size, cities, initialise=False)
        
        # Keep the best route if elitism is enabled
        elitism_offset = 0
        if self.elitism:
            new_population.save_route(0, pop.get_fittest())
            elitism_offset = 1
        
        # Crossover population
        for i in range(elitism_offset, new_population.size):
            # Select parents
            parent1 = self.tournament_selection(pop)
            parent2 = self.tournament_selection(pop)
            
            # Crossover
            child = self.crossover(parent1, parent2, cities)
            
            # Mutate
            if random.random() < self.mutation_probability:
                child = self.mutate(child)
            
            new_population.save_route(i, child)
        
        return new_population

    def tournament_selection(self, pop: RoutePop) -> Route:
        """
        Select a route using tournament selection.
        
        Args:
            pop (RoutePop): Population to select from
            
        Returns:
            Route: Selected route
        """
        tournament = RoutePop(self.tournament_size, [], initialise=False)
        
        # Randomly select routes for tournament
        for i in range(self.tournament_size):
            random_id = random.randint(0, pop.size - 1)
            tournament.save_route(i, pop.get_route(random_id))
        
        # Return the fittest
        return tournament.get_fittest()

    def crossover(self, parent1: Route, parent2: Route, cities: List[City]) -> Route:
        """
        Perform ordered crossover between two parents.
        
        Args:
            parent1 (Route): First parent route
            parent2 (Route): Second parent route
            cities (List[City]): List of cities
            
        Returns:
            Route: Child route
        """
        child = Route(cities)  # This will be overwritten
        start_pos = random.randint(0, len(cities) - 1)
        end_pos = random.randint(0, len(cities) - 1)
        
        if start_pos > end_pos:
            start_pos, end_pos = end_pos, start_pos
        
        # Copy segment from parent1
        for i in range(start_pos, end_pos + 1):
            child.route[i] = parent1.route[i]
        
        # Fill remaining positions with cities from parent2
        current_pos = (end_pos + 1) % len(cities)
        for city in parent2.route:
            if city not in child.route[start_pos:end_pos + 1]:
                child.route[current_pos] = city
                current_pos = (current_pos + 1) % len(cities)
        
        child.recalc_rt_len()
        return child

    def mutate(self, route: Route) -> Route:
        """
        Perform swap mutation on a route.
        
        Args:
            route (Route): Route to mutate
            
        Returns:
            Route: Mutated route
        """
        route_copy = Route(route.route)  # Create a copy
        pos1 = random.randint(0, len(route.route) - 1)
        pos2 = random.randint(0, len(route.route) - 1)
        
        # Swap cities
        route_copy.route[pos1], route_copy.route[pos2] = route_copy.route[pos2], route_copy.route[pos1]
        route_copy.recalc_rt_len()
        
        return route_copy 