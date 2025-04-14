# Traveling Salesman Problem Solver

This project implements two algorithms for solving the Traveling Salesman Problem (TSP):
1. Branch and Bound algorithm
2. Genetic Algorithm

## Features

- Solve TSP using either Branch and Bound or Genetic Algorithm
- Input cities via JSON file with coordinates
- Convert Russian cities data to TSP format
- Filter cities by population
- Visualize the resulting route
- Configurable algorithm parameters

## Requirements

- Python 3.7+
- Required packages:
  - numpy
  - matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/travel_salesman_problem.git
cd travel_salesman_problem
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### City Data Conversion

The project includes a script to convert Russian cities data into the TSP format:

```bash
# Convert all cities with population > 500,000
python convert_cities.py russian-cities.json cities.json

# Convert cities with custom population threshold
python convert_cities.py russian-cities.json cities.json --min-population 1000000

# Convert top N largest cities
python convert_cities.py russian-cities.json cities.json --max-cities 20
```

The script will:
1. Read the input JSON file with Russian cities data
2. Filter cities by population (default > 500,000)
3. Sort cities by population
4. Save the result in TSP format

### TSP Solver

The main script `main.py` accepts the converted JSON file and allows choosing between algorithms.

Basic usage with Branch and Bound:
```bash
python main.py --input cities.json --algorithm branch_and_bound
```

Using Genetic Algorithm with custom parameters:
```bash
python main.py --input cities.json --algorithm genetic --population-size 100 --generations 500
```

### Command Line Arguments

#### City Conversion (`convert_cities.py`)

Required arguments:
- `input_file`: Path to input JSON file with Russian cities data
- `output_file`: Path to output JSON file in TSP format

Optional arguments:
- `--min-population`: Minimum population threshold (default: 500000)
- `--max-cities`: Maximum number of cities to include

#### TSP Solver (`main.py`)

Required arguments:
- `-i, --input`: Path to JSON file containing city coordinates

Optional arguments:
- `-a, --algorithm`: Algorithm to use (`branch_and_bound` or `genetic`, default: `branch_and_bound`)
- `-o, --output`: Path to save the solution as JSON
- `--no-plot`: Disable route visualization

Genetic Algorithm parameters:
- `-p, --population-size`: Size of the population (default: 100)
- `-g, --generations`: Number of generations (default: 500)
- `-m, --mutation-prob`: Probability of mutation (default: 0.02)
- `-t, --tournament-size`: Size of tournament selection (default: 5)
- `--no-elitism`: Disable elitism (enabled by default)

Branch and Bound parameters:
- `--bnb-time-limit`: Time limit in seconds (default: 60.0)

### Example Workflow

1. Convert Russian cities data:
```bash
python convert_cities.py russian-cities.json cities.json --min-population 500000
```

2. Run the TSP solver:
```bash
python main.py --input cities.json --algorithm genetic --population-size 200 --generations 1000
```

3. The script will:
   - Load the cities from the JSON file
   - Run the selected algorithm
   - Display the results
   - Show a visualization of the route
   - Save the solution to a JSON file if requested

## Output

### City Conversion
- Console output with:
  - Number of cities converted
  - Largest and smallest cities in the dataset
  - Population statistics

### TSP Solver
- Console output with:
  - Algorithm parameters
  - Time taken
  - Total distance
  - Route order
- Visual plot of the route
- Optional JSON output with the solution

## License

This project is licensed under the MIT License - see the LICENSE file for details. 