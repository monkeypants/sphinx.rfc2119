# -*- coding: utf-8 -*-
"""
sphinx.util.compat
~~~~~~~~~~~~~~~~~~

Stuff for docutils compatibility.

:copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
:license: BSD, see LICENSE for details.

vendored from sphinx repository
"""

from docutils import nodes
from docutils.parsers.rst import Directive  # noqa

from docutils import __version__ as _du_version

docutils_version = tuple(int(x) for x in _du_version.split(".")[:2])


def make_admonition(
    node_class,
    name,
    arguments,
    options,
    content,
    lineno,
    content_offset,
    block_text,
    state,
    state_machine,
):
    text = "\n".join(content)
    admonition_node = node_class(text)
    if arguments:
        title_text = arguments[0]
        textnodes, messages = state.inline_text(title_text, lineno)
        admonition_node += nodes.title(title_text, "", *textnodes)
        admonition_node += messages
        if "class" in options:
            classes = options["class"]
        else:
            classes = ["admonition-" + nodes.make_id(title_text)]
        admonition_node["classes"] += classes
    state.nested_parse(content, content_offset, admonition_node)
    return [admonition_node]
