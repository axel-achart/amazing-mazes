import heapq
from typing import List, Tuple, Optional, Set
from labyrinth.lab_to_jpg import convert_solution_to_image

class Node:
    def __init__(self, position: Tuple[int, int], g_cost: float = 0, h_cost: float = 0, parent=None):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

def load_maze_from_file(filename: str) -> Optional[List[List[str]]]:
    try:
        with open(f"labyrinth/{filename}.txt", 'r') as file:
            return [list(row) for row in file.read().strip().split('\n')]
    except FileNotFoundError:
        print(f"Error: File 'labyrinth/{filename}.txt' does not exist.")
        return None

def find_start_and_end(maze: List[List[str]]) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    start = end = None
    rows, cols = len(maze), len(maze[0]) if maze else 0
    for col in range(cols):
        if maze[0][col] == '.':
            start = (0, col)
            break
    for col in range(cols):
        if maze[rows-1][col] == '.':
            end = (rows-1, col)
            break
    return start, end

def heuristic(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(position: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:
    row, col = position
    rows, cols = len(maze), len(maze[0])
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
            neighbors.append((nr,nc))
    return neighbors

def reconstruct_path(node: Node) -> List[Tuple[int, int]]:
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]

def a_star_solver(maze: List[List[str]], start: Tuple[int,int], end: Tuple[int,int]) -> Optional[Tuple[List[Tuple[int,int]], Set[Tuple[int,int]]]]:
    open_set = []
    closed_set: Set[Tuple[int,int]] = set()
    start_node = Node(start, 0, heuristic(start,end))
    heapq.heappush(open_set, start_node)
    g_costs = {start:0}
    nodes_explored = 0

    while open_set:
        current_node = heapq.heappop(open_set)
        current_pos = current_node.position
        if current_pos == end:
            return reconstruct_path(current_node), closed_set
        closed_set.add(current_pos)
        nodes_explored += 1
        for neighbor in get_neighbors(current_pos, maze):
            if neighbor in closed_set:
                continue
            tentative_g = current_node.g_cost + 1
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                heapq.heappush(open_set, Node(neighbor, tentative_g, heuristic(neighbor,end), current_node))
    return None

def visualize_solution(maze: List[List[str]], path: List[Tuple[int,int]], explored: Set[Tuple[int,int]]) -> str:
    visual_maze = [row[:] for row in maze]
    for r,c in explored:
        if (r,c) not in path:
            visual_maze[r][c] = 'O'
    for i,(r,c) in enumerate(path):
        if i == 0: visual_maze[r][c] = 'S'
        elif i == len(path)-1: visual_maze[r][c] = 'E'
        else: visual_maze[r][c] = '*'
    return '\n'.join(''.join(row) for row in visual_maze)

def solve_maze_astar(filename: str) -> bool:
    maze = load_maze_from_file(filename)
    if maze is None:
        return False
    start, end = find_start_and_end(maze)
    if start is None or end is None:
        print("Error: Maze entrance or exit not found.")
        return False
    result = a_star_solver(maze, start, end)
    if result:
        path, explored = result
        solution_visual = visualize_solution(maze, path, explored)
        solution_filename = f"{filename}_solution_astar"
        with open(f"labyrinth/solutions_astar/{solution_filename}.txt", 'w') as f:
            f.write(solution_visual)
        print(f"Solution saved in labyrinth/solutions_astar/{solution_filename}.txt")
        print(solution_visual)
        convert_solution_to_image(filename, "astar")
        return True
    else:
        print("No path found.")
        return False
