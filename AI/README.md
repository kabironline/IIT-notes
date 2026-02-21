# Nearest Neighbour Heuristic Script

This folder contains a simple Python script (`code.py`) implementing the **Nearest Neighbour heuristic** for constructing a tour over a fully connected weighted graph (e.g. a Travelling Salesman Problem instance).

## Purpose

Given a set of `n` locations and their pairwise distance (or cost) matrix, the script:

1. Reads the problem instance from standard input.
2. Builds a tour starting from node `0` using the Nearest Neighbour greedy rule.
3. Prints the resulting tour as a space-separated list of zero-based node indices (length `n`).

## File Overview

| File      | Description                                                                         |
| --------- | ----------------------------------------------------------------------------------- |
| `code.py` | Core implementation: input parsing + nearest neighbour heuristic + main entry point |

## Input Format (from stdin)

The program expects lines in the following order:

1. A string token describing the distance type (e.g. `EUCLIDEAN`, `EXPLICIT`, etc.). Stored but not used in the current logic.
2. An integer `n` = number of cities.
3. Next `n` lines: Each line has attributes for one location (the script just parses them into a list of floats; their semantics are not used by the heuristic). Example: `10.0 42.7`.
4. Next `n` lines: Each line contains `n` floating-point numbers representing one row of the distance matrix. Row `i`, column `j` is the distance (or cost) from city `i` to city `j`.

### Example Input

```
EUCLIDEAN
4
0.0 0.0
1.0 0.0
1.0 1.0
0.0 1.0
0 1 2 1
1 0 1 2
2 1 0 1
1 2 1 0
```

Explanation:

- Distance type: `EUCLIDEAN` (ignored)
- `n = 4`
- 4 location lines (coordinates). Not used by the solver.
- 4x4 symmetric distance matrix.

### Output

A single line: the space-separated tour (list of node indices) produced by the heuristic, starting at node 0. For the sample above, one possible output is:

```
0 1 2 3
```

(Exact order depends on tie-breaking by Python's `min`; with equal distances it picks the lowest index.)

## Core Function: `nearest_neighbour_heuristic(graph, start_node, n)`

- `graph`: 2D list (matrix) where `graph[i][j]` is the cost from `i` to `j`.
- `start_node`: integer index to start from (always `0` in current usage).
- `n`: number of nodes.

Algorithm steps:

1. Initialize the set of unvisited nodes to all except `start_node`.
2. Start the tour with `[start_node]`.
3. While unvisited nodes remain:
   - Select the node `j` in `unvisited` minimizing `graph[current][j]`.
   - Append it to the tour, mark as visited, and move `current` to `j`.
4. Return the tour (length `n`).

Note: The tour is **not closed**; it omits returning to the start. If you need a cycle, append the start node at the end when printing.

## Complexity

- Each of the `n-1` selection steps scans the remaining unvisited nodes: O(n) each.
- Total time complexity: O(n^2).
- Space complexity: O(n) for the `unvisited` set and tour list (excluding the input matrix itself which is O(n^2)).

## Limitations / Notes

- Greedy heuristic: does not guarantee optimality for TSP; can be arbitrarily worse than optimal in some cases.
- Tie-breaking: chooses the lowest-index node among equals due to Python's ordering in `min` with a key.
- Assumes a complete distance matrix with non-negative numeric entries.
- Does not validate input sizes or numeric ranges.
- Ignores the raw `locations` and the `distance_type` value—only the matrix is used.
- Produces a path, not a closed tour.

## Possible Improvements

- Add option to close the tour by returning to start and printing total distance.
- Incorporate coordinates to compute distances on the fly if matrix not provided.
- Add input validation and clearer error messages.
- Allow specifying a different starting node via CLI argument.
- Implement alternative heuristics (e.g., 2-opt improvement, cheapest insertion) for better solution quality.
- Provide a seedable deterministic tie-breaker or randomized restarts.

## Minimal Usage (interactive)

Run the script and enter data when prompted (or pipe a prepared file):

```
python code.py < sample_input.txt
```

(Adjust command if your Python executable is named differently.)

## Verifying Total Distance (Optional Extension)

To compute the path length afterward:

```python
# Suppose 'tour' was printed as: 0 1 2 3
order = [0,1,2,3]
length = sum(dist[order[i]][order[i+1]] for i in range(len(order)-1))
# If you want to close the loop:
length_cycle = length + dist[order[-1]][order[0]]
```

## Quick Reference

- Input: distance type line, n, n location lines, n distance-matrix lines.
- Output: one line with n integers (0..n-1) = visit order.
- Algorithm: Nearest neighbour greedy path (not closed).

---

Feel free to adapt or extend this script for coursework experiments with heuristics.
