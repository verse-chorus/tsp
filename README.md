# Traveling Salesman Problem Solver

This project implements two algorithms for solving the Traveling Salesman Problem (TSP):
1. Branch and Bound algorithm
2. Genetic Algorithm

## Example
Here's an example of optimal route created by genetic algorithm for russian cities with more that 250000 citizens.
![image](https://github.com/user-attachments/assets/2e1834d6-89a3-44df-9a08-b37a47925f57)
```bash
Loading cities from .\data\russian_cities250k.json...
Loaded 79 cities

Running Genetic Algorithm...

Genetic Algorithm Parameters:
Population size: 100
Number of generations: 500
Mutation probability: 0.02
Tournament size: 5
Elitism: enabled

Genetic Algorithm Results:
Total distance: 420.48 units

Route order:
1. Нижний Тагил
2. Пермь
3. Магнитогорск
4. Оренбург
5. Набережные Челны
6. Киров
7. Чебоксары
..
74. Нижневартовск
75. Томск
76. Омск
77. Сургут
78. Курган
79. Челябинск
```

## Features

- Solve TSP using either Branch and Bound or Genetic Algorithm
- Input cities via JSON file with coordinates
- Visualize the resulting route
- Configurable algorithm parameters

## Requirements

- Python 3.7+
- Required packages:
  - `numpy`
  - `matplotlib`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tsp.git
cd tsp
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

The main script `main.py` accepts a JSON file containing city coordinates and allows choosing between algorithms.

### Input JSON Format

Create a JSON file (e.g., `cities.json`) with the following format:
```json
{
    "cities": [
        {"name": "City1", "x": 10.0, "y": 20.0},
        {"name": "City2", "x": 30.0, "y": 40.0},
        ...
    ]
}
```

### Running the Solver

Basic usage with Branch and Bound:
```bash
python main.py --input cities.json --algorithm bnb
```

Using Genetic Algorithm with custom parameters:
```bash
python main.py --input cities.json --algorithm genetic --population-size 100 --generations 500
```

### Command Line Arguments

Required arguments:
- `-i, --input`: Path to JSON file containing city coordinates

Optional arguments:
- `-a, --algorithm`: Algorithm to use (`bnb` or `genetic`, default: `bnb`)
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

### Example

1. Create a JSON file with city coordinates:
```json
{
    "cities": [
        {"name": "Moscow", "x": 55.7558, "y": 37.6173},
        {"name": "Saint Petersburg", "x": 59.9343, "y": 30.3351},
        {"name": "Novosibirsk", "x": 55.0084, "y": 82.9357}
    ]
}
```

2. Run the solver:
```bash
python main.py --input cities.json --algorithm genetic --population-size 50 --generations 200
```

3. The script will:
   - Load the cities from the JSON file
   - Run the selected algorithm
   - Display the results
   - Show a visualization of the route
   - Save the solution to a JSON file if requested

## Output

The script provides:
1. Console output with:
   - Algorithm parameters
   - Time taken
   - Total distance
   - Route order
2. Visual plot of the route
3. Optional JSON output with the solution

## License
`russian-cities.json` was copied from [this repo](https://github.com/pensnarik/russian-cities)
