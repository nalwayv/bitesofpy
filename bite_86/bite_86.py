"""
Bite 86. Create a RGB-to-Hex converter
"""


def rgb_to_hex(rgb) -> str:
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0
    """

    RED = 16
    GREEN = 8
    BLUE = 0
    r, g, b = rgb

    # out of range
    if r < 0 or r >= 256 or g < 0 or g >= 256 or b < 0 or b >= 256:
        raise ValueError("out of range")

    hex_it = hex((r << RED) + (g << GREEN) + (b << BLUE))[2:]

    if len(hex_it) < 6:
        return f"#{'0'*(6-len(hex_it))}{hex_it}".upper()
    return f"#{hex_it}".upper()


if __name__ == "__main__":
    print(rgb_to_hex((0, 0, 0)))  # black
    print(rgb_to_hex((255, 255, 255)))  # white
    print(rgb_to_hex((255, 0, 0)))  # red
    print(rgb_to_hex((0, 255, 0)))  # lime
    print(rgb_to_hex((0, 0, 255)))  # blue
    print(rgb_to_hex((255, 255, 0)))  # yellow
    print(rgb_to_hex((0, 255, 255)))  # cyan / aqua
    print(rgb_to_hex((255, 0, 255)))  # magenta / fuchsia
    print(rgb_to_hex((192, 192, 192)))  # silver
    print(rgb_to_hex((128, 128, 128)))  # gray
    print(rgb_to_hex((128, 0, 0)))  # maroon
    print(rgb_to_hex((128, 128, 0)))  # olive
    print(rgb_to_hex((0, 128, 0)))  # green
    print(rgb_to_hex((128, 0, 128)))  # purple
    print(rgb_to_hex((0, 128, 128)))  # teal
    print(rgb_to_hex((0, 0, 128)))  # navy
