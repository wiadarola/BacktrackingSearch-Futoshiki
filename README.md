# Futoshiki Puzzle Solver using Backtracking Search (CSPs)

An AI project dedicated to solving the Futoshiki puzzle leveraging the power of Constraint Satisfaction Problems (CSPs) and backtracking search.

## Table of Contents
- [Overview](#overview)
- [Algorithm](#algorithm)
- [Installation](#installation)
- [Usage](#usage)

## Overview

The Futoshiki puzzle is a logic puzzle from Japan, similar to Sudoku, but with inequality constraints. This project aims to solve the Futoshiki puzzle by applying the principles of Constraint Satisfaction Problems (CSPs) combined with backtracking search.

## Algorithm

Utilizing backtracking search, which is a form of depth-first search where the solution space is navigated systematically, the algorithm assigns values within constraints until a solution is found or the assignment is deemed incorrect. With CSPs, the solver ensures that the assigned values meet the puzzle's constraints.

## Installation

1. Clone this repository: 
```
git clone https://github.com/your_username/futoshiki-solver.git
```

2. Navigate to the directory:
```
cd futoshiki-solver
```

## Usage

To solve a Futoshiki puzzle, provide a text file with the puzzle configuration and run the `futoshiki.py` script:

```
python futoshiki.py path_to_input_file.txt
```
