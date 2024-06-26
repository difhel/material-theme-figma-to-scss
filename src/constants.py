COLORS = ["primary", "secondary", "tertiary", "neutral", "neutral-variant", "error"]
THEMES = ["light", "dark"]
COPYRIGHT = """/* Generated automatically by material-theme-figma-to-css (https://github.com/difhel/material-theme-figma-to-scss)
Author: Mark Fomin aka @difhel (email material-theme-figma-to-scss@difhel.dev)
2024
*/

"""
SDFUI_STYLES = """/* ✨ @nacteam/sdfui styles ✨ */
html {
    font-family: 'Google Sans', 'Product Sans', 'TT Norms', 'Roboto', sans-serif;
    font-size: 14pt;
    background: var(--background);
}

"""
SHAPES = {
    "--shape-none": "0",
    "--shape-extra-small": "4px",
    "--shape-small": "8px",
    "--shape-medium": "12px",
    "--shape-large": "16dp",
    "--shape-extra-large": "28px",
    "--shape-full": "100%",
}
BORDERS = {
    "--border-none": "none",
    "--border-outline": "1px solid var(--outline)",
    "--border-outline-variant": "1px solid var(--outline-variant)",
}
ELEVATION = {
    "light": {
        "--elevation-1": "0px 1px 3px 1px rgba(0, 0, 0, 0.15), 0px 1px 2px 0px rgba(0, 0, 0, 0.30)",
        "--elevation-2": "0px 2px 6px 2px rgba(0, 0, 0, 0.15), 0px 1px 2px 0px rgba(0, 0, 0, 0.30)",
        "--elevation-3": "0px 1px 3px 0px rgba(0, 0, 0, 0.30), 0px 4px 8px 3px rgba(0, 0, 0, 0.15)",
        "--elevation-4": "0px 2px 3px 0px rgba(0, 0, 0, 0.30), 0px 6px 10px 4px rgba(0, 0, 0, 0.15)",
        "--elevation-5": "0px 4px 4px 0px rgba(0, 0, 0, 0.30), 0px 8px 12px 6px rgba(0, 0, 0, 0.15)"
    },
    "dark": {
       "--elevation-1": "0px 1px 2px 0px rgba(0, 0, 0, 0.30), 0px 1px 3px 1px rgba(0, 0, 0, 0.15)",
       "--elevation-2": "0px 1px 2px 0px rgba(0, 0, 0, 0.30), 0px 2px 6px 2px rgba(0, 0, 0, 0.15)",
       "--elevation-3": "0px 1px 3px 0px rgba(0, 0, 0, 0.30), 0px 4px 8px 3px rgba(0, 0, 0, 0.15)",
       "--elevation-4": "0px 2px 3px 0px rgba(0, 0, 0, 0.30), 0px 6px 10px 4px rgba(0, 0, 0, 0.15)",
       "--elevation-5": "0px 4px 4px 0px rgba(0, 0, 0, 0.30), 0px 8px 12px 6px rgba(0, 0, 0, 0.15)"
    }
}