from typing import List, Tuple, Optional, Set
import time
from labyrinth.lab_to_jpg import convert_solution_to_image

def load_maze_from_file(filename: str) -> Optional[List[List[str]]]:
    try:
        with open(f"labyrinth/{filename}.txt", 'r') as file:
            return [list(row) for row in file.read().strip().split('\n')]
    except FileNotFoundError:
        print(f"Error: File 'labyrinth/{filename}.txt' does not exist.")
        return None

def find_start_and_end(maze: List[List[str]]) -> Tuple[Optional[Tuple[int,int]], Optional[Tuple[int,int]]]:
    start = end = None
    rows, cols = len(maze), len(maze[0]) if maze else 0
    for col in range(cols):
        if maze[0][col] == '.':
            start = (0,col)
            break
    for col in range(cols):
        if maze[rows-1][col] == '.':
            end = (rows-1,col)
            break
    return start, end

def get_neighbors(pos: Tuple[int,int], maze: List[List[str]]) -> List[Tuple[int,int]]:
    r,c = pos
    rows,cols = len(maze), len(maze[0])
    neighbors=[]
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc = r+dr,c+dc
        if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]=='.':
            neighbors.append((nr,nc))
    return neighbors

def recu_backtracking_solver(maze: List[List[str]], start: Tuple[int,int], end: Tuple[int,int]) -> Optional[Tuple[List[Tuple[int,int]], Set[Tuple[int,int]]]]:
    nodes_explored = 0
    max_depth = 0
    explored_cells = set()

    def backtrack(current, path, visited, depth) -> bool:
        nonlocal nodes_explored, max_depth
        nodes_explored += 1
        max_depth = max(max_depth, depth)
        explored_cells.add(current)
        if current == end:
            return True
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                path.append(neighbor)
                if backtrack(neighbor, path, visited, depth+1):
                    return True
                path.pop()
        visited.remove(current)
        return False

    path = [start]
    visited = set()
    start_time = time.time()
    if backtrack(start,path,visited,0):
        print(f"Path found! Length: {len(path)}, Nodes explored: {nodes_explored}, Max depth: {max_depth}, Time: {time.time()-start_time:.3f}s")
        return path, explored_cells
    print(f"No path found. Nodes explored: {nodes_explored}, Time: {time.time()-start_time:.3f}s")
    return None

def visualize_solution(maze: List[List[str]], path: List[Tuple[int,int]], explored: Set[Tuple[int,int]]) -> str:
    visual_maze = [row[:] for row in maze]
    for r,c in explored:
        if (r,c) not in path:
            visual_maze[r][c] = 'O'
    for i,(r,c) in enumerate(path):
        if i==0: visual_maze[r][c]='S'
        elif i==len(path)-1: visual_maze[r][c]='E'
        else: visual_maze[r][c]='*'
    return '\n'.join(''.join(row) for row in visual_maze)

def solve_maze_backtracking(filename: str) -> bool:
    maze = load_maze_from_file(filename)
    if maze is None:
        return False
    start,end=find_start_and_end(maze)
    if start is None or end is None:
        print("Error: Maze entrance or exit not found.")
        return False
    result=recu_backtracking_solver(maze,start,end)
    if result:
        path, explored = result
        solution_visual = visualize_solution(maze,path,explored)
        solution_filename = f"{filename}_solution_backtracking"
        with open(f"labyrinth/solutions_backtracking/{solution_filename}.txt",'w') as f:
            f.write(solution_visual)
        print(f"Solution saved in labyrinth/solutions_backtracking/{solution_filename}.txt")
        print(solution_visual)
        convert_solution_to_image(filename,"backtracking")
        return True
    else:
        return False
