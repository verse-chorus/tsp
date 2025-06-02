"""
Visualization utilities for the Traveling Salesman Problem.
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from typing import List
from .route import Route
from .city import City

def plot_route(route: Route, title: str = "Traveling Salesman Problem Solution") -> None:
    """
    Plot a route using matplotlib, treating coordinates as latitude and longitude.
    
    Args:
        route (Route): Route to plot
        title (str): Title of the plot
    """
    plt.figure(figsize=(12, 8))
    
    # Get coordinates, treating y as longitude and x as latitude
    latitudes = [city.x for city in route.route]
    longitudes = [city.y for city in route.route]
    
    # Plot the route
    plt.plot(longitudes + [longitudes[0]], latitudes + [latitudes[0]], 'b-', alpha=0.5)
    plt.scatter(longitudes, latitudes, c='red', s=100)
    
    # Add city labels with adjusted positioning
    for city in route.route:
        plt.annotate(city.name, 
                    (city.y, city.x),
                    xytext=(10, 10),
                    textcoords='offset points')
    
    plt.title(title)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    
    # Set aspect ratio to be closer to Mercator projection
    plt.gca().set_aspect(1.0/plt.gca().get_data_ratio())
    
    plt.show()

def plot_route_on_globe(route: Route, title: str = "TSP Solution on Globe") -> None:
    """
    Plot a route on a spherical projection of Earth using cartopy.
    
    Args:
        route (Route): Route to plot
        title (str): Title of the plot
    """
    # Create figure with orthographic projection centered on Russia
    # First argument is central longitude (100°E), second is central latitude (60°N)
    plt.figure(figsize=(15, 15))
    ax = plt.axes(projection=ccrs.Orthographic(100, 60))
    
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.gridlines()
    
    # Get coordinates
    latitudes = [city.x for city in route.route]
    longitudes = [city.y for city in route.route]
    
    # Plot route
    # Convert route coordinates to map projection
    ax.plot(longitudes + [longitudes[0]], 
           latitudes + [latitudes[0]], 
           'b-', 
           transform=ccrs.Geodetic(),
           alpha=0.5,
           linewidth=2)
    
    # Plot cities
    ax.scatter(longitudes, 
              latitudes, 
              c='red', 
              s=100, 
              transform=ccrs.Geodetic(),
              zorder=5)
    
    # Add city labels with improved visibility
    for city in route.route:
        ax.text(city.y, city.x,
                city.name,
                transform=ccrs.Geodetic(),
                horizontalalignment='left',
                verticalalignment='top',
                zorder=6)
    
    plt.title(title)
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