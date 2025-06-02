# Traveling Salesman Problem Solver

A Python implementation of the Traveling Salesman Problem (TSP) solver using two different algorithms: Branch and Bound and Genetic Algorithm. This project provides an efficient way to find optimal or near-optimal routes for visiting multiple cities.

## Installation

```bash
git clone https://github.com/yourusername/tsp.git
conda create -name <env_name>
conda init
conda activate <env_name>
pip install -r requirements.txt
cd ./tsp/src
```

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

- Two solving algorithms:
  - Branch and Bound (exact solution)
  - Genetic Algorithm (heuristic solution)
- Visual route plotting
- JSON input/output support
- Configurable algorithm parameters
- Efficient distance calculations

## Requirements

- Python 3.7+
- Required packages:
  - numpy==1.26.4
  - matplotlib==3.4.0
  - pandas==1.3.0


## Usage
### Input Format

The program expects a JSON file containing city coordinates in the following format:
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

Basic usage with default parameters:
```bash
python main.py --input cities.json
```

Using **Branch and Bound** algorithm:
```bash
python main.py \
--input cities.json \
--algorithm bnb
```

Using **Genetic Algorithm** with custom parameters:
```bash
python main.py \
--input cities.json \
--algorithm genetic \
--population-size 100 \
--generations 500 \
--mutation-prob 0.02
```

### Command Line Arguments

- `-i, --input`: Path to JSON file containing city coordinates (required)
- `-a, --algorithm`: Algorithm to use ('bnb' or 'genetic', default: 'genetic')
- `-p, --population-size`: Population size for genetic algorithm (default: 100)
- `-g, --generations`: Number of generations for genetic algorithm (default: 500)
- `-m, --mutation-prob`: Mutation probability (0.0 to 1.0, default: 0.02)
- `-t, --tournament-size`: Tournament size for selection (default: 5)
- `--no-elitism`: Disable elitism in genetic algorithm
- `--bnb-time-limit`: Time limit in seconds for branch and bound (default: 60.0)
- `--no-plot`: Disable route visualization
- `-o, --output`: Path to save the solution as JSON

## Output

The program provides:
1. Console output with:
   - Algorithm parameters
   - Total distance of the route
   - Time taken (for Branch and Bound)
   - Route order
2. Visual plot of the route (unless disabled)
3. JSON file with the solution (if output path is specified)

## Example

```bash
python main.py \
--input data/cities.json \
--algorithm genetic \
--population-size 200 \
--generations 1000 \
--mutation-prob 0.01 \
--output solution.json
```

This will:
1. Load cities from `data/cities.json`
2. Run the genetic algorithm with the specified parameters
3. Display the results in the console
4. Show a plot of the route
5. Save the solution to `solution.json`

## License
`russian-cities.json` was copied from [this repo](https://github.com/pensnarik/russian-cities/tree/master)