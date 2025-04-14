"""
Example script demonstrating the TSP solver with sample data.

Usage:
    python example.py --population-size 100 --generations 500 --mutation-prob 0.02 --tournament-size 5
"""

from tsp import City, GeneticAlgorithm, BranchAndBound, plot_route, plot_convergence
import time
import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Solve Traveling Salesman Problem using different algorithms',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
    
    # General parameters
    parser.add_argument(
        '--no-plot',
        action='store_true',
        help='Disable route visualization'
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

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Create sample cities (coordinates of major Russian cities)
    cities = [
        City("Moscow", 55.7558, 37.6173),
        City("Saint Petersburg", 59.9343, 30.3351),
        City("Novosibirsk", 55.0084, 82.9357),
        City("Yekaterinburg", 56.8389, 60.6057),
        City("Kazan", 55.7961, 49.1064),
        City("Nizhny Novgorod", 56.3268, 44.0065),
        City("Chelyabinsk", 55.1644, 61.4368),
        City("Omsk", 54.9914, 73.3645),
        City("Samara", 53.1959, 50.1002),
        City("Rostov-on-Don", 47.2225, 39.7187)
    ]

    print("Traveling Salesman Problem Solver")
    print("=================================")
    print(f"Number of cities: {len(cities)}")
    
    # Calculate distances between all cities
    print("\nCalculating distances between cities...")
    for city in cities:
        city.calculate_distances(cities)

    # Run Branch and Bound algorithm
    print("\nRunning Branch and Bound algorithm...")
    bnb = BranchAndBound()
    bnb_route, bnb_time = bnb.run(cities, time_limit=args.bnb_time_limit)
    
    print("\nBranch and Bound Results:")
    print(f"Time taken: {bnb_time:.2f} seconds")
    print(f"Total distance: {bnb_route.length:.2f} units")
    print("\nRoute order:")
    for i, city in enumerate(bnb_route.route, 1):
        print(f"{i}. {city.name}")

    # Run Genetic Algorithm
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

    start_time = time.time()
    ga_route = ga.run(cities, args.generations)
    ga_time = time.time() - start_time
    
    print("\nGenetic Algorithm Results:")
    print(f"Time taken: {ga_time:.2f} seconds")
    print(f"Total distance: {ga_route.length:.2f} units")
    print("\nRoute order:")
    for i, city in enumerate(ga_route.route, 1):
        print(f"{i}. {city.name}")

    # Compare results
    print("\nComparison:")
    print(f"Branch and Bound: {bnb_route.length:.2f} units in {bnb_time:.2f} seconds")
    print(f"Genetic Algorithm: {ga_route.length:.2f} units in {ga_time:.2f} seconds")
    print(f"Difference: {abs(bnb_route.length - ga_route.length):.2f} units")
    print(f"Time difference: {abs(bnb_time - ga_time):.2f} seconds")

    # Visualize the results if not disabled
    if not args.no_plot:
        plot_route(bnb_route, title="Branch and Bound Solution")
        plot_route(ga_route, title="Genetic Algorithm Solution")

if __name__ == "__main__":
    main() 