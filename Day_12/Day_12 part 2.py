import random

def list_of_hexa_colors(count):
    hex_chars = '0123456789abcdef'
    colors = []
    for _ in range(count):
        code = '#' + ''.join(random.choices(hex_chars, k=6))
        colors.append(code)
    return colors
print(list_of_hexa_colors(3))
def list_of_rgb_colors(count):
    colors = []
    for _ in range(count):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")   
    return colors
print(list_of_rgb_colors(3))
def generate_colors(color_type, count):
    if color_type == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
