from PIL import Image
import os

def txt_to_image(txt_file, output_file, cell_size=20):
    with open(txt_file, "r") as f:
        lines = [line.strip() for line in f]
    h, w = len(lines), len(lines[0])
    img = Image.new("RGB", (w * cell_size, h * cell_size), "white")
    pixels = img.load()
    
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                color = (0, 0, 0)   
            elif char == "*":
                color = (0, 0, 255)   
            elif char == "O":
                color = (255, 0, 0)    
            elif char == "S":
                color = (0, 255, 0)   
            elif char == "E":
                color = (255, 255, 0)   
            else:
                color = (255, 255, 255)  
            for dy in range(cell_size):
                for dx in range(cell_size):
                    pixels[x * cell_size + dx, y * cell_size + dy] = color

    img.save(output_file)
    print(f"Image saved as {output_file}")

def convert_solution_to_image(filename: str, algorithm: str):
    algorithm = algorithm.lower()
    if algorithm == "astar":
        folder = "solutions_astar"
        suffix = "_solution_astar"
    elif algorithm == "backtracking":
        folder = "solutions_backtracking"
        suffix = "_solution_backtracking"
    else:
        print("Unknown algorithm. Use 'astar' or 'backtracking'.")
        return
    
    txt_path = f"labyrinth/{folder}/{filename}{suffix}.txt"
    jpg_path = f"labyrinth/{folder}/{filename}{suffix}.jpg"
    
    if not os.path.exists(txt_path):
        print(f"File not found: {txt_path}")
        return

    answer = input(f"Do you want to convert the {algorithm} solution to JPG? (y/n): ").strip().lower()
    if answer == "y":
        txt_to_image(txt_path, jpg_path)
    else:
        print("Conversion skipped.")

if __name__ == "__main__":
    maze_name = input("Enter the maze filename (without .txt): ").strip()
    algo = input("Which solution do you want to convert? (astar/backtracking): ").strip().lower()
    convert_solution_to_image(maze_name, algo)
