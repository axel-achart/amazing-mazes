# Display Menu in Terminal
from labyrinth.generate import generationlabyrinth
from labyrinth.generate_file import generate_file
from labyrinth.lab_to_jpg import txt_to_image


def display_labyrinth():
    print("\nWelcome to Amazing Mazes, labyrinths of  Minotaur\n")
    labyrinth_content = generationlabyrinth()
    txt_path = generate_file(labyrinth_content)
    txt_to_image(txt_path, f"labyrinth/{labyrinth_content}.jpg")
    return


def display_menu():
    print("\n1. Recursive Backtracking Solver")
    print("2. AStar Solver")
    choose = int(input("\nChoose a solver for the labyrinth : "))


    if choose not in (1, 2):
        print("\nInvalid choice. Please select a valid option.")
        print("-------------------------------")
        return display_menu()
    
    if choose == 1:
        pass

    elif choose == 2:
        pass


if __name__ == "__main__":
    display_labyrinth()
    display_menu()