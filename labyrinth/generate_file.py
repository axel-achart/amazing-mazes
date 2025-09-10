
def generate_file(content):
    name_file = str(input("Enter the name of the file: "))

    with open(f"labyrinth/{name_file}.txt", 'w') as file:
        file.write(content)
    print(f"File '{name_file}.txt' has been created inside labyrinth/ folder.")
    
    return name_file