# Display Menu in Terminal
from labyrinth.generate import generationlabyrinth
from labyrinth.generate_file import generate_file
from algorithm.a_star import solve_maze_astar
from algorithm.recu_backtraking import solve_maze_backtracking
from labyrinth.lab_to_jpg import txt_to_image


def display_labyrinth():
    print("\nWelcome to Amazing Mazes, labyrinths of the Minotaur\n")
    labyrinth_content = generationlabyrinth()
    txt_path = generate_file(labyrinth_content)

    display_img = input("\nDo you want to convert labyrinth generated ASCII into an image? (y/n): ").strip().lower()
    if display_img == 'y':
        output_file = txt_path.replace(".txt", ".jpg")  
        txt_to_image(txt_path, output_file)
    else:
        return


def display_menu():
    print("\n" + "="*60)
    print("  AMAZING MAZES - SOLVER MENU  ")
    print("="*60)
    print("1.  Recursive Backtracking Solver")
    print("2.  A* (A-Star) Solver")
    print("3.  Solve existing maze file")
    print("4.  Exit")
    print("="*60)
    
    try:
        choose = int(input("\nChoose a solver for the labyrinth: "))
    except ValueError:
        print("\n Invalid input. Please enter a number.")
        print("-" * 30)
        return display_menu()

    if choose not in (1, 2, 3, 4):
        print("\n Invalid choice. Please select a valid option (1-4).")
        print("-" * 30)
        return display_menu()
    
    if choose == 1:
        print("\n Recursive Backtracking Solver selected!")
        return "backtracking"

    elif choose == 2:
        print("\n A* Solver selected!")
        return "astar"
    
    elif choose == 3:
        print("\n Solve existing maze file")
        return "existing"
    
    elif choose == 4:
        print("\n Thank you for using Amazing Mazes!")
        return "exit"


def solve_existing_maze():
    print("\n Loading existing maze...")
    filename = input("Enter the name of the maze file (without .txt): ")
    
    if not filename.strip():
        print(" Invalid filename.")
        return False
    
    # Ask which algorithm to use
    print("\n Choose solving algorithm:")
    print("1.  Recursive Backtracking")
    print("2.  A*")
    
    try:
        algo_choice = int(input("Your choice (1 or 2): "))
    except ValueError:
        print(" Invalid choice, using A* by default.")
        algo_choice = 2
    
    if algo_choice == 1:
        return solve_maze_backtracking(filename)
    else:
        return solve_maze_astar(filename)


def compare_algorithms(filename: str):
    print(f"\n === COMPARISON OF ALGORITHMS === ")
    print(f"Maze: {filename}.txt\n")
    
    print("=" * 70)
    print(" SOLVING WITH RECURSIVE BACKTRACKING:")
    print("=" * 70)
    success_bt = solve_maze_backtracking(filename)
    
    print("\n" + "=" * 70)
    print(" SOLVING WITH A*:")
    print("=" * 70)
    success_astar = solve_maze_astar(filename)
    
    print("\n" + "=" * 70)
    print(" SUMMARY OF COMPARISON:")
    print("=" * 70)
    print(f"Recursive Backtracking: {' Success' if success_bt else ' Failure'}")
    print(f"A*:                     {' Success' if success_astar else ' Failure'}")


def main():
    print(" " * 25)
    print("    Welcome to AMAZING MAZES")
    print("    The Labyrinths of the Minotaur")
    print(" " * 25)
    
    while True:
        print("\n" + "="*60)
        print(" MAIN MENU")
        print("="*60)
        print("1.  Generate and solve new maze")
        print("2.  Solve existing maze")
        print("3.  Compare algorithms on existing maze")
        print("4.  Exit")
        
        try:
            main_choice = int(input("\nYour choice: "))
        except ValueError:
            print(" Please enter a valid number.")
            continue
        
        if main_choice == 1:
            # Generate a new maze
            filename = display_labyrinth()
            if filename:
                solver_choice = display_menu()
                
                if solver_choice == "astar":
                    print(f"\n Solving maze '{filename}' with A*...")
                    success = solve_maze_astar(filename)
                    if success:
                        print("\n Maze solved successfully with A*!")
                    else:
                        print("\n Failed to solve the maze with A*.")
                
                elif solver_choice == "backtracking":
                    print(f"\n Solving maze '{filename}' with Recursive Backtracking...")
                    success = solve_maze_backtracking(filename)
                    if success:
                        print("\n Maze solved successfully with Recursive Backtracking!")
                    else:
                        print("\n Failed to solve the maze with Recursive Backtracking.")
                
                elif solver_choice == "existing":
                    solve_existing_maze()
                
                elif solver_choice == "exit":
                    break
        
        elif main_choice == 2:
            # Solve an existing maze
            solve_existing_maze()
        
        elif main_choice == 3:
            # Compare algorithms
            print("\n Loading maze for comparison...")
            filename = input("Enter the name of the maze file (without .txt): ")
            if filename.strip():
                compare_algorithms(filename)
            else:
                print(" Invalid filename.")
        
        elif main_choice == 4:
            print("\n Thank you for using Amazing Mazes!")
            print("May you always find your way out of the labyrinth! ")
            break
        
        else:
            print(" Invalid choice. Please select 1, 2, 3, or 4.")
        
        # Ask if the user wants to continue
        if main_choice in [1, 2, 3]:
            while True:
                continue_choice = input("\nDo you want to continue? (y/n): ").lower().strip()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\n Thank you for using Amazing Mazes!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()