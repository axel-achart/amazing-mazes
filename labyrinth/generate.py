# generate.py
import random
import time, tracemalloc

def generationlabyrinth():
    size_input = input("Enter the size of the labyrinth (between 5 - 15) : ")
    try:
        size = int(size_input)
        """if not (5 <= size <= 15):
            print("Please enter a valid number between 5 and 15.")
            return generationlabyrinth()"""
    except ValueError:
        print("Invalid input. Please enter a number.")
        return generationlabyrinth()

    # Correction size to be odd (no pair)
    if size % 2 == 0:
        old = size
        size -= 1
        if size < 3:
            size = 3
        print(f"Size {old} adjusted to nearest odd size {size} for correct maze generation.")

    # Choice of algorithm
    algo = input("Choose algorithm (dfs / kruskal) : ").strip().lower()
    if algo not in ["dfs", "kruskal"]:
        print("Invalid choice. Please choose 'dfs' or 'kruskal'.")
        return generationlabyrinth()

    # ALGO DFS BACKTRACKING
    def generate_dfs(size):
        start = time.perf_counter()
        tracemalloc.start()
        tracemalloc.reset_peak()
        maze = [["#" for _ in range(size)] for _ in range(size)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y):
            return 0 < x < size - 1 and 0 < y < size - 1

        def carve(x, y):
            maze[y][x] = "."
            order = dirs[:]
            random.shuffle(order)
            for dx, dy in order:
                nx, ny = x + dx * 2, y + dy * 2
                if is_valid(nx, ny) and maze[ny][nx] == "#":
                    maze[y + dy][x + dx] = "."
                    carve(nx, ny)

        carve(1, 1)
        end = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Maze generated in {end - start:.4f} seconds.")
        print(f"Current memory usage is {peak[0] / 10**6:.4f}MB; Peak was {peak[1] / 10**6:.4f}MB")
        return maze

    # ALGO KRUSKAL
    def generate_kruskal(size):
        start = time.perf_counter()
        tracemalloc.start()
        tracemalloc.reset_peak()
        maze = [["#" for _ in range(size)] for _ in range(size)]

        # Create cells and sets
        cells = [(x, y) for y in range(1, size, 2) for x in range(1, size, 2)]
        sets = {cell: cell for cell in cells}

        def find(cell):
            while sets[cell] != cell:
                sets[cell] = sets[sets[cell]]
                cell = sets[cell]
            return cell

        def union(a, b):
            sets[find(a)] = find(b)

        walls = []
        for x, y in cells:
            if x + 2 < size:
                walls.append(((x, y), (x + 2, y), (x + 1, y)))
            if y + 2 < size:
                walls.append(((x, y), (x, y + 2), (x, y + 1)))

        random.shuffle(walls)

        for cell1, cell2, wall in walls:
            if find(cell1) != find(cell2):
                union(cell1, cell2)
                x1, y1 = cell1
                x2, y2 = cell2
                wx, wy = wall
                maze[y1][x1] = "."
                maze[y2][x2] = "."
                maze[wy][wx] = "."

        end = time.perf_counter()
        peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Maze generated in {end - start:.4f} seconds.")
        print(f"Current memory usage is {peak[0] / 10**6:.4f}MB; Peak was {peak[1] / 10**6:.4f}MB")
        return maze

    # Select and generate maze
    if algo == "dfs":
        maze = generate_dfs(size)
    else:
        maze = generate_kruskal(size)

    # Add entry and exit
    entry_col = next((c for c in range(1, size - 1) if maze[1][c] == "."), 1)
    maze[0][entry_col] = "."
    exit_col = next((c for c in range(size - 2, 0, -1) if maze[size - 2][c] == "."), size - 2)
    maze[size - 1][exit_col] = "."

    return "\n".join("".join(row) for row in maze)