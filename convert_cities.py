"""
Script to convert Russian cities JSON format into TSP solver format.
"""

import json
from typing import Dict, List

def convert_city(city_data: Dict, min_population: int = 500000) -> Dict:
    """
    Convert a single city from the input format to the TSP format.
    
    Args:
        city_data (Dict): City data in the input format
        min_population (int): Minimum population threshold
        
    Returns:
        Dict: City data in the TSP format, or None if population is below threshold
    """
    try:
        population = int(city_data["population"])
        if population < min_population:
            return None
            
        return {
            "name": city_data["name"],
            "x": float(city_data["coords"]["lat"]),
            "y": float(city_data["coords"]["lon"]),
            "population": population
        }
    except (KeyError, ValueError) as e:
        print(f"Warning: Could not convert city {city_data.get('name', 'unknown')}: {e}")
        return None

def convert_json(input_file: str, output_file: str, max_cities: int = None, min_population: int = 500000) -> None:
    """
    Convert cities from input JSON format to TSP format.
    
    Args:
        input_file (str): Path to input JSON file
        output_file (str): Path to output JSON file
        max_cities (int, optional): Maximum number of cities to include. Defaults to None (all cities).
        min_population (int): Minimum population threshold. Defaults to 500000.
    """
    # Read input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        cities_data = json.load(f)
    
    # Convert cities
    tsp_cities = []
    for city_data in cities_data:
        tsp_city = convert_city(city_data, min_population)
        if tsp_city is not None:
            tsp_cities.append(tsp_city)
            
            # Stop if we've reached the maximum number of cities
            if max_cities and len(tsp_cities) >= max_cities:
                break
    
    # Sort cities by population (descending)
    tsp_cities.sort(key=lambda x: x["population"], reverse=True)
    
    # Write output JSON
    output_data = {"cities": tsp_cities}
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully converted {len(tsp_cities)} cities with population > {min_population:,} to {output_file}")
    print(f"Largest city: {tsp_cities[0]['name']} ({tsp_cities[0]['population']:,} people)")
    print(f"Smallest city: {tsp_cities[-1]['name']} ({tsp_cities[-1]['population']:,} people)")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert Russian cities JSON to TSP format')
    parser.add_argument('input_file', help='Path to input JSON file')
    parser.add_argument('output_file', help='Path to output JSON file')
    parser.add_argument('--max-cities', type=int, help='Maximum number of cities to include')
    parser.add_argument('--min-population', type=int, default=500000, help='Minimum population threshold')
    
    args = parser.parse_args()
    
    convert_json(args.input_file, args.output_file, args.max_cities, args.min_population)

if __name__ == "__main__":
    main() 