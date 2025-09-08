# Display Menu in Terminal

def display_menu():
    print("\nWelcome to Amazing Mazes, labyrinths of  Minotaur\n")
    print("1. Recursive Backtracking Solver")
    print("2. AStar Solver")
    print("3. ASCII Solver")
    print("4. Kruskal Solver")
    choose = input("\nChoose a solver for the labyrinth : ")


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
    display_menu()