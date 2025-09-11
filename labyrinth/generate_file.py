
def generate_file(content):
    name_file = str(input("Enter the name of the file: "))
    path = f"labyrinth/{name_file}.txt"

    with open(path, 'w') as file:
        file.write(content)
    print(f"File '{path}' has been created inside labyrinth/ folder.")
    
    return path