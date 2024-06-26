from requests import Response

def read_from_stdin_or_file(filename: str, message: str) -> str:
    value = input(f"{message} (Enter to read value from `{filename}`): ")
    if not value:
        try:
            with open(filename) as file:
                value = file.read().strip()
        except FileNotFoundError:
            print(f"[Error] File `{filename}` not found.")
            exit(1)
    else:
        with open(filename, "w") as file:
            file.write(value)
        print(f"Saved value to `{filename}`.")
    return value

def request_figma_api(response: Response) -> dict:
    if response.status_code != 200:
        print(f"[Error] Figma API returned an error: {response.json()}")
        exit(1)
    return response.json()

def rgba_to_hex(rgba_color: str, opacity: float | None = None) -> str:
    r = int(rgba_color["r"] * 255)
    g = int(rgba_color["g"] * 255)
    b = int(rgba_color["b"] * 255)
    if opacity is None:
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    else:
        opacity_hex = int(opacity * 255)
        hex_color = "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, opacity_hex)

    return hex_color

def get_color_name(text: str) -> tuple[str, int]:
    """Parse color name and number from the full color name

    Args:
        text (str): full color name

    Returns:
        tuple[str, int]: color name and the number
    
    Example:
        get_color_name("primary100") -> ("primary", 100)
    """
    index = next(i for i, c in enumerate(text) if c.isdigit())
    color_name = text[:index]
    color_num = int(text[index:])
    return color_name, color_num

