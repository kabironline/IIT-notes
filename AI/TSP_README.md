# TSP Heuristic Solver Documentation

## Overview

This script provides a fast heuristic solution for the Travelling Salesman Problem (TSP) using a combination of the Nearest Neighbour algorithm and 2-Opt local search. It is designed to read a problem instance from standard input, construct multiple tours, and iteratively improve them within a time budget.

## Features

- **Input parsing**: Accepts both bulk and interactive input formats for flexibility.
- **Nearest Neighbour**: Greedy tour construction from multiple randomized start nodes.
- **2-Opt**: Local search to improve tours by edge swaps.
- **Multi-start**: Tries up to 32 different starting nodes for better solutions.
- **Time control**: Respects a time limit via the `TSP_TIME_LIMIT` environment variable.
- **Deterministic randomness**: Uses a seed (`TSP_SEED`) for reproducible results.
- **Streaming output**: Prints every new best tour found.

## Input Format

The script expects the following input (whitespace-separated, from stdin):

```
DIST_TYPE
N
x0 y0
x1 y1
...
x{N-1} y{N-1}
d00 d01 ... d0{N-1}
d10 d11 ... d1{N-1}
...
d{N-1}0 ... d{N-1}{N-1}
```

- `DIST_TYPE`: String describing the distance type (e.g., `EUC_2D`).
- `N`: Number of cities.
- Next `N` lines: Coordinates for each city (not used in computation, but parsed).
- Next `N` lines: Distance matrix (NxN floats).

If stdin is empty, the script falls back to interactive line-by-line input.

## Output Format

- Each line: a space-separated list of city indices (zero-based) representing a tour.
- Only prints a new line if a strictly better tour is found (lower cost).

## Algorithm Details

### Nearest Neighbour

- Starts from a given node.
- At each step, selects the closest unvisited city.
- Time complexity: O(N^2).

### 2-Opt

- Iteratively swaps edges to reduce tour cost.
- Stops when no further improvement is possible or time runs out.
- Time complexity: O(N^2) per pass, but limited by time budget.

### Multi-start

- Always starts with node 0.
- Randomly shuffles other nodes and tries up to 32 starts.
- Each start is followed by Nearest Neighbour and optional 2-Opt.

## Time and Randomness Control

- `TSP_TIME_LIMIT`: Maximum allowed runtime in seconds (default: 295, clamped between 1 and 295).
- `TSP_SEED`: Seed for randomization (default: 42).

## Edge Cases

- If input is malformed, prints a trivial tour (0 1 2 ... N-1).
- Assumes distance matrix is complete and non-negative.

## Example Usage

```bash
python tsp_solver.py < input.txt
```

Set a time limit:

```bash
set TSP_TIME_LIMIT=10
python tsp_solver.py < input.txt
```
