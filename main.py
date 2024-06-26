import os
import requests
from dataclasses import dataclass

from src.utils import read_from_stdin_or_file, request_figma_api, rgba_to_hex, get_color_name

from src.constants import COLORS, SDFUI_STYLES, THEMES, COPYRIGHT, SHAPES, BORDERS, ELEVATION

token = read_from_stdin_or_file("token.txt", "[1] Your Figma access token")

file_url = read_from_stdin_or_file("file_url.txt", "[2] Your Figma URL")
file_id = file_url.split("figma.com/")[-1].split("/")[1]

is_sdfui = input("Is this @nacteam/sdfui styles? (y/n): ") == "y"

print("Step 1. Getting local styles list")
value = request_figma_api(requests.get(
    f"https://api.figma.com/v1/files/{file_id}/styles", headers={"X-Figma-Token": token}
))

@dataclass
class FigmaColorToken:
    name: str
    node_id: str


material_colors: list[FigmaColorToken] = []  # [ [color_name: str, node_id: str] ]
for style in value["meta"]["styles"]:
    if not (style["style_type"] == "FILL" and style["name"].startswith("md3/")):
        continue
    material_colors.append(FigmaColorToken(style["name"], style["node_id"]))


print("Step 2. Getting values")
res = request_figma_api(requests.get(
    f"https://api.figma.com/v1/files/{file_id}/nodes",
    headers={"X-Figma-Token": token},
    params={
        "ids": ",".join(color.node_id for color in material_colors)
    },
))

print("Step 3. Exporting colors to CSS file...")
styles = {}
for node in res["nodes"]:
    color_name = res["nodes"][node]["document"]["name"]
    color_value = rgba_to_hex(res["nodes"][node]["document"]["fills"][0]["color"])
    styles[color_name] = color_value

ref_colors = {color: [] for color in COLORS}
theme_tokens = {theme: {} for theme in THEMES}

for k, v in styles.items():
    if k.startswith("md3/ref/"):
        color = k.split("/")[-1]
        color_name, color_num = get_color_name(color)
        ref_colors[color_name].append((color_num, v))
    if k.startswith("md3/sys/dark") or k.startswith("md3/sys/light"):
        color_name = k.split("/")[-1]
        color_theme = k.split("/")[-2]
        if is_sdfui and any(color_name.startswith(x) for x in [
            "primary", "secondary", "tertiary", "surface", "error"
        ]):
            # In sdfui, we need to add alpha channel to background colors
            # 75% alpha channel is 0xBF
            v += "bf"
        theme_tokens[color_theme][color_name] = v

for theme in THEMES:
    theme_tokens[theme] = dict(sorted(theme_tokens[theme].items(), key=lambda x: x[0]))

for color in COLORS:
    ref_colors[color] = list(sorted(ref_colors[color], key=lambda x: x[0]))

colors = []
for theme_type in COLORS:
    colors.append(f"/* {theme_type.capitalize()} colors */\n")
    colors.append("html {\n")
    for color in ref_colors[theme_type]:
        colors.append(f"    --{theme_type}-{color[0]}: {color[1]};\n")
    colors.append("}\n\n")

themes = []
for theme_type in THEMES:
    themes.append(f"html:has(* > .{theme_type}) " + "{\n")
    for color_name, color_value in theme_tokens[theme_type].items():
        themes.append(f"    --{color_name}: {color_value};\n")
    for elevation_level, elevation_value in ELEVATION[theme_type].items():
        themes.append(f"    {elevation_level}: {elevation_value};\n")
    themes.append("}\n\n")

with open("output.module.scss", "w") as file:
    file.write(COPYRIGHT)
    if is_sdfui:
        file.write(SDFUI_STYLES)
    file.write(":global {\n")
    for c in colors:
        file.write("    " + c)
    for c in themes:
        file.write("    " + c)
    file.write("\n    /* Elevation tokens */\n")
    file.write("    html { \n")
    for shape, value in SHAPES.items():
        file.write(f"        {shape}: {value};\n")
    file.write("    }\n\n")
    file.write("    /* Border tokens */\n")
    file.write("    html { \n")
    for border, value in BORDERS.items():
        file.write(f"        {border}: {value};\n")
    file.write("    }\n")
    file.write("}")

print(f"Done. The colors have been written to {os.getcwd()}/output.module.scss")
