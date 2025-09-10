# Display Menu in Terminal
from labyrinth.generate import generationlabyrinth
from labyrinth.generate_file import generate_file


def display_labyrinth():
    print("\nWelcome to Amazing Mazes, labyrinths of  Minotaur\n")
    labyrinth_content = generationlabyrinth()
    generate_file(labyrinth_content)
    return


def display_menu():
    print("\n1. Recursive Backtracking Solver")
    print("2. AStar Solver")
    print("3. ASCII Solver")
    print("4. Kruskal Solver")
    choose = int(input("\nChoose a solver for the labyrinth : "))


    if choose not in (1, 2, 3, 4):
        print("\nInvalid choice. Please select a valid option.")
        print("-------------------------------")
        return display_menu()
    
    if choose == 1:
        pass

    elif choose == 2:
        pass

    elif choose == 3:
        pass

    elif choose == 4:
        pass


if __name__ == "__main__":
    display_labyrinth()
    display_menu()