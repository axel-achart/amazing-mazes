# 🌀 Amazing Mazes – Minotaur’s Labyrinths

## 📖 Project Overview

Inspired by the legend of Daedalus and the Minotaur, this project demonstrates the design of a **maze generator** and **solver** that creates perfect mazes—structures with one unique path between any two points.  
The project blends core algorithmic logic, data visualization, and automated solving, making it ideal for learners and technical enthusiasts interested in computational problem-solving.

---

## ⚙️ Key Features

### Maze Generation

- Implements two advanced algorithms:
  - **DFS (Backtracking):** Step-by-step path carving for random maze creation.
  - **Kruskal:** Generates mazes by merging cells until the grid is fully connected.
- Outputs:
  - ASCII format: `#` for walls, `.` for open paths.
  - Optional: Maze visualization as JPG images for enhanced clarity and presentations.

### Automated Solving & Exploration

- Includes two robust solvers:
  - **Recursive Backtracking:** Explores every possible route to find a solution.
  - **A\*** (A-Star): Finds the optimal path using heuristic-based search.
- Visual indicators:
  - `o` marks the discovered optimal path.
  - `*` shows all explored cells.

### Advanced Visualization & Benchmarking

- Converts ASCII mazes into images (using **Pillow**)
- Performance testing on mazes up to size **4500**
- Side-by-side comparisons of generation and solving times for each algorithm

---

## 📊 Observed Results

### Maze Generation

| Algorithm | Memory Usage | Notes                                      |
|-----------|--------------|--------------------------------------------|
| Kruskal   | Higher       | Best for generating very large mazes       |
| DFS       | Moderate     | Similar speed; always outputs odd sizes    |

### Maze Solving

| Solver                | Speed        | Memory  | Notes                                     |
|-----------------------|-------------|---------|-------------------------------------------|
| A*                    | Faster      | Moderate| Handles large mazes (up to size < 1000)   |
| Recursive Backtracking| Slower      | Higher  | Less efficient for large mazes            |

---

## 🛠️ Technologies & Stack

- **Python** (core logic and scripts)
- **Pillow** (image processing and visualization)
- **Algorithms**: Backtracking (DFS), Kruskal’s Algorithm, and A*

---
