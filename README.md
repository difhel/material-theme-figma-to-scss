# Material Theme Figma to SCSS Module Converter

This script converts the color styles created by the Material Theme Builder plugin in Figma into a SCSS module file.

This option is better than https://m3.material.io/theme-builder -> Export as Web (CSS), because the official export function still doesn't support the new tone-based surfaces introduced by the Material Design team on **March 23, 2023**. This script, unlike the official export function, supports the new surface colors (`surface-container-low`, etc) and the new colors introduced (`primary-fixed`, `primary-fixed-dim`, etc). More details here: https://material.io/blog/tone-based-surface-color-m3.

It exports all Material Design styles to `output.module.scss` file, so you can import it and use with your SCSS code.

This code generator is used by [nacteam/sdfui](https://github.com/nacteam/sdfui) UI library.

# Run
To run this script, you need the following things:
* ## Access token
    Go to https://figma.com, user profile -> Settings -> Account -> Personal access tokens -> Generate new token
    ![1](./screenshots/1.png)
    ![2](./screenshots/2.png)
* ## Figma URL
    * Open your Figma file
    * Search for the plugin "Material Theme Builder"

        ![3](./screenshots/3.png)
    * Select 3 key colors and build a theme
    
        ![4](./screenshots/4.png)
    * Check that your theme was converted to color styles

        ![5](./screenshots/5.png)
    * Share -> Copy link

        ![6](./screenshots/6.png)

```bash
$ git clone https://github.com/difhel/material-theme-figma-to-css
$ cd material-theme-figma-to-css
$ pip install requests
$ python3 main.py
> [1] Your Figma access token (Enter to read value from `token.txt`): figd_***_**
> [2] Your Figma URL (Enter to read value from `file_url.txt`): https://www.figma.com/file/************************/******?type=design&node-id=0%3A1&mode=design
Step 1. Getting local styles list
Step 2. Getting values
Step 3. Exporting colors to CSS file...
Done. The colors have been written to /home/mf/material-theme-figma-to-scss/output.module.scss
```

You can see an example of generated CSS-file [here](https://github.com/difhel/material-theme-figma-to-scss/blob/master/output.module.scss).