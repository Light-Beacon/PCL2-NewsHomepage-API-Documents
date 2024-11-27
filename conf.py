# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# region Compile Less
import subprocess
import shutil
from pathlib import Path

def compile_less_to_css():
    less_path = Path("_styles")
    css_path = Path("_generated/styles")
    shutil.rmtree(css_path)
    less_files = list(less_path.rglob("*.less"))
    for less_file in less_files:
        css_file = css_path / less_file.relative_to(less_path).with_suffix(".css")
        subprocess.run(["lessc", str(less_file), str(css_file),
                        "--source-map","--source-map-include-source"], check=True)
        print(f'Compling {less_file.name}')

compile_less_to_css()
# endregion

project = 'PCL2-NewsHomepage-API'
copyright = '2024, Light-Beacon'
author = 'Light-Beacon'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx_copybutton']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static','_generated']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    'styles/custom.css',
    'styles/httpmethods.css'
]

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#extensions.append("sphinx_wagtail_theme")
html_theme = 'furo' #press #sphinx_book_theme #sphinx_wagtail_theme #furo

html_theme_options = {
    "source_repository": "https://github.com/Light-Beacon/PCL2-NewsHomepage-API-Documents",
    "source_branch": "master",
    "source_directory": ".",
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Light-Beacon/PCL2-NewsHomepage-API-Documents",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x footer-icon",
        },
    ],
}
