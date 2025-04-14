"""
City module for the Traveling Salesman Problem.
"""

import math
from typing import Dict, List, Optional

class City:
    """
    Represents a city in the Traveling Salesman Problem.
    
    Attributes:
        name (str): Name of the city
        x (float): X-coordinate of the city
        y (float): Y-coordinate of the city
        distance_to (Dict[str, float]): Dictionary of distances to other cities
    """
    
    def __init__(self, name: str, x: float, y: float, distance_to: Optional[Dict[str, float]] = None):
        """
        Initialize a City object.
        
        Args:
            name (str): Name of the city
            x (float): X-coordinate
            y (float): Y-coordinate
            distance_to (Dict[str, float], optional): Pre-calculated distances to other cities
        """
        self.name = name
        self.x = self.graph_x = x
        self.y = self.graph_y = y
        self.distance_to = {self.name: 0.0}
        if distance_to:
            self.distance_to = distance_to

    def calculate_distances(self, cities: List['City']) -> None:
        """
        Calculate distances from this city to all other cities.
        
        Args:
            cities (List[City]): List of all cities to calculate distances to
        """
        for city in cities:
            if city.name != self.name:
                tmp_dist = self.point_dist(self.x, self.y, city.x, city.y)
                self.distance_to[city.name] = tmp_dist

    @staticmethod
    def point_dist(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        Calculate Euclidean distance between two points.
        
        Args:
            x1 (float): X-coordinate of first point
            y1 (float): Y-coordinate of first point
            x2 (float): X-coordinate of second point
            y2 (float): Y-coordinate of second point
            
        Returns:
            float: Euclidean distance between the points
        """
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def __repr__(self) -> str:
        return f"City({self.name}, x={self.x}, y={self.y})" 