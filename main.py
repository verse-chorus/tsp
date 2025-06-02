"""
Traveling Salesman Problem Solver

This script solves the Traveling Salesman Problem using either Branch and Bound or Genetic Algorithm.
It accepts a JSON file containing city coordinates as input.

Usage:
    python main.py --input cities.json --algorithm bnb
    python main.py --input cities.json --algorithm genetic --population-size 100 --generations 500
"""

import json
import argparse
from typing import List, Dict
from src import City, GeneticAlgorithm, BranchAndBound, plot_route, plot_route_on_globe

def load_cities_from_json(json_file: str) -> List[City]:
    """
    Load cities from a JSON file.
    
    Expected JSON format:
    {
        "cities": [
            {"name": "City1", "x": 10.0, "y": 20.0},
            {"name": "City2", "x": 30.0, "y": 40.0},
            ...
        ]
    }
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cities = []
    for city_data in data['cities']:
        city = City(city_data['name'], city_data['x'], city_data['y'])
        cities.append(city)
    
    # Calculate distances between all cities
    for city in cities:
        city.calculate_distances(cities)
    
    return cities

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Solve Traveling Salesman Problem using different algorithms',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Path to JSON file containing city coordinates'
    )
    
    parser.add_argument(
        '-a', '--algorithm',
        type=str,
        choices=['bnb', 'genetic'],
        default='genetic',
        help='Algorithm to use for solving TSP: branch and bound (bnb) or genetic (genetic)'
    )
    
    # Genetic Algorithm parameters
    parser.add_argument(
        '-p', '--population-size',
        type=int,
        default=100,
        help='Size of the population for genetic algorithm'
    )
    
    parser.add_argument(
        '-g', '--generations',
        type=int,
        default=500,
        help='Number of generations to run for genetic algorithm'
    )
    
    parser.add_argument(
        '-m', '--mutation-prob',
        type=float,
        default=0.02,
        help='Probability of mutation (0.0 to 1.0)'
    )
    
    parser.add_argument(
        '-t', '--tournament-size',
        type=int,
        default=5,
        help='Size of tournament selection'
    )
    
    parser.add_argument(
        '--no-elitism',
        action='store_true',
        help='Disable elitism (by default elitism is enabled)'
    )
    
    # Branch and Bound parameters
    parser.add_argument(
        '--bnb-time-limit',
        type=float,
        default=60.0,
        help='Time limit in seconds for branch and bound algorithm'
    )
    
    # Output options
    parser.add_argument(
        '--no-plot',
        action='store_true',
        help='Disable route visualization'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Path to save the solution as JSON'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not 0 <= args.mutation_prob <= 1:
        parser.error("Mutation probability must be between 0 and 1")
    
    if args.tournament_size > args.population_size:
        parser.error("Tournament size cannot be larger than population size")
    
    if args.population_size < 2:
        parser.error("Population size must be at least 2")
    
    if args.generations < 1:
        parser.error("Number of generations must be at least 1")
        
    return args

def save_solution_to_json(route, output_file: str):
    """Save the solution route to a JSON file."""
    solution = {
        "total_distance": route.length,
        "route": [
            {
                "name": city.name,
                "x": city.x,
                "y": city.y
            }
            for city in route.route
        ]
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(solution, f, indent=4, ensure_ascii=False)

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Load cities from JSON
    print(f"Loading cities from {args.input}...")
    cities = load_cities_from_json(args.input)
    print(f"Loaded {len(cities)} cities")
    
    # Run selected algorithm
    if args.algorithm == 'bnb':
        print("\nRunning Branch and Bound algorithm...")
        bnb = BranchAndBound()
        route, time_taken = bnb.run(cities, time_limit=args.bnb_time_limit)
        
        print("\nBranch and Bound Results:")
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Total distance: {route.length:.2f} units")
        
    else:  # genetic algorithm
        print("\nRunning Genetic Algorithm...")
        print("\nGenetic Algorithm Parameters:")
        print(f"Population size: {args.population_size}")
        print(f"Number of generations: {args.generations}")
        print(f"Mutation probability: {args.mutation_prob}")
        print(f"Tournament size: {args.tournament_size}")
        print(f"Elitism: {'disabled' if args.no_elitism else 'enabled'}")
        
        ga = GeneticAlgorithm(
            population_size=args.population_size,
            mutation_probability=args.mutation_prob,
            tournament_size=args.tournament_size,
            elitism=not args.no_elitism
        )
        
        route = ga.run(cities, args.generations)
        
        print("\nGenetic Algorithm Results:")
        print(f"Total distance: {route.length:.2f} units")
    
    # Print route
    print("\nRoute order:")
    for i, city in enumerate(route.route, 1):
        print(f"{i}. {city.name}")
    
    # Save solution if requested
    if args.output:
        print(f"\nSaving solution to {args.output}...")
        save_solution_to_json(route, args.output)
    
    # Plot route if not disabled
    if not args.no_plot:
        plot_route(route, title=f"{args.algorithm.title()} Solution")
        plot_route_on_globe(route, "Маршрут по городам России")

if __name__ == "__main__":
    main() 