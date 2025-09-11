from PIL import Image

def txt_to_image(txt_file, output_file, cell_size=20):
    with open(txt_file, "r") as f:
        lines = [line.strip() for line in f]

    h, w = len(lines), len(lines[0])
    img = Image.new("RGB", (w * cell_size, h * cell_size), "white")
    pixels = img.load()

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            color = (0, 0, 0) if char == "#" else (255, 255, 255)
            for dy in range(cell_size):
                for dx in range(cell_size):
                    pixels[x * cell_size + dx, y * cell_size + dy] = color

    img.save(output_file)
    print(f"Image saved as {output_file}")