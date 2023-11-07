import os
import requests

COLORS = ["primary", "secondary", "tertiary", "neutral", "neutral-variant", "error"]
THEMES = ["light", "dark"]
COPYRIGHT = """/* Generated automatically by material-theme-figma-to-css (https://github.com/difhel/material-theme-figma-to-css)
Author: Mark Fomin aka @difhel (email material-theme-figma-to-css@difhel.dev)
2023
* /
"""

token = input("[1] Your Figma access token: ")
file_id = input("[2] Your Figma URL: ").split("/file/")[-1].split("/")[0]
print("Step 1. Getting local styles list")
r = requests.get(f"https://api.figma.com/v1/files/{file_id}/styles", headers={
    "X-Figma-Token": token
})

value = r.json()
material_colors = [] # [ [color_name: str, node_id: str] ]
for style in value["meta"]["styles"]:
    if not (style["style_type"] == "FILL" and style["name"].startswith("md3/")): continue
    material_colors.append((style["name"], style["node_id"]))


print("Step 2. Getting values")
r = requests.get(f"https://api.figma.com/v1/files/{file_id}/nodes", headers={
    "X-Figma-Token": token
}, params={
    "ids": ",".join([material_colors[i][1] for i in range(len(material_colors))])
})

def rgba_to_hex(rgba_color):
    r = int(rgba_color["r"] * 255)
    g = int(rgba_color["g"] * 255)
    b = int(rgba_color["b"] * 255)
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    return hex_color

def get_color_name(text):
    index = next(i for i, c in enumerate(text) if c.isdigit())
    return text[:index]

res = r.json()
print("Step 3. Exporting colors to CSS file...")
styles = {}
for node in res["nodes"]:
    color_name = res["nodes"][node]["document"]["name"]
    color_value = rgba_to_hex(res["nodes"][node]["document"]["fills"][0]["color"])
    styles[color_name] = color_value

ref_colors = {
    color: [] for color in COLORS
}
theme_tokens = {
    theme: {} for theme in THEMES
}

for k, v in styles.items():
    if k.startswith("md3/ref/"):
        color = k.split("/")[-1]
        color_name = get_color_name(color)
        color_num = int(color.split(color_name)[-1])
        ref_colors[color_name].append((color_num, v))
    if k.startswith("md3/sys/dark") or k.startswith("md3/sys/light"):
        color_name = k.split("/")[-1]
        color_theme = k.split("/")[-2]
        theme_tokens[color_theme][color_name] = v

for color in COLORS:
    ref_colors[color] = list(sorted(ref_colors[color], key = lambda x: x[0]))

colors = []
for theme_type in COLORS:
    colors.append(f"/* {theme_type.capitalize()} colors */")
    colors.append("\nhtml {\n")
    for color in ref_colors[theme_type]:
        colors.append(f"    --{theme_type}-{color[0]}: {color[1]};\n")
    colors.append("}\n\n")

themes = []
for theme_type in THEMES:
    themes.append(f"html:has(* > .{theme_type})")
    themes.append(" {\n")
    for color_name, color_value in theme_tokens[theme_type].items():
        themes.append(f"    --{color_name}: {color_value};\n")
    themes.append("}\n\n")

with open("output.css", "w") as file:
    file.write(COPYRIGHT)
    for c in colors:
        file.write(c)
    for c in themes:
        file.write(c)
print("Done. The colors have been written to {os.getcwd()}/output.css")