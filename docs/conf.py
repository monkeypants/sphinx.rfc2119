import sys
import os

sys.path.append(os.path.abspath("."))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_rfc2119",
]
rfc2119_include_mandatorys = True
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "sphinx.rfc2119"
copyright = "2015, Chris Gough"
author = "Chris Gough"
version = "0.1"
release = "0.1"
language = "en"
exclude_patterns = ["_build", "*venv**"]
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
htmlhelp_basename = "sphinxrfc2119doc"
latex_elements = {
    "papersize": "a4paper",
}

latex_documents = [
    (
        master_doc,
        "sphinxrfc2119.tex",
        "sphinx.rfc2119 Documentation",
        "Chris Gough",
        "manual",
    ),
]

man_pages = [(master_doc, "sphinxrfc2119", "sphinx.rfc2119 Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "sphinxrfc2119",
        "sphinx.rfc2119 Documentation",
        author,
        "sphinxrfc2119",
        "One line description of project.",
        "Miscellaneous",
    ),
]
