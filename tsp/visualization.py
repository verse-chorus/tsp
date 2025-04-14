"""
Visualization utilities for the Traveling Salesman Problem.
"""

import matplotlib.pyplot as plt
from typing import List
from .route import Route
from .city import City

def plot_route(route: Route, title: str = "Traveling Salesman Problem Solution") -> None:
    """
    Plot a route using matplotlib.
    
    Args:
        route (Route): Route to plot
        title (str): Title of the plot
    """
    plt.figure(figsize=(10, 6))
    
    # Plot cities
    x_coords = [city.x for city in route.route]
    y_coords = [city.y for city in route.route]
    
    # Plot the route
    plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], 'b-', alpha=0.5)
    plt.scatter(x_coords, y_coords, c='red', s=100)
    
    # Add city labels
    for city in route.route:
        plt.annotate(city.name, (city.x, city.y), 
                    xytext=(5, 5), textcoords='offset points')
    
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.show()

def plot_convergence(fitness_history: List[float], title: str = "Fitness Convergence") -> None:
    """
    Plot the convergence of the genetic algorithm.
    
    Args:
        fitness_history (List[float]): List of best fitness values over generations
        title (str): Title of the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(fitness_history)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Route Length")
    plt.grid(True)
    plt.show() 