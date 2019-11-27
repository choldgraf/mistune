from .markdown import Markdown
from .block_parser import BlockParser
from .inline_parser import InlineParser
from .renderers import AstRenderer, HTMLRenderer
from .scanner import escape, escape_url, escape_html, unikey
from .plugins import PLUGINS


def create_markdown(escape=True, renderer=None, plugins=None):
    """Create a Markdown instance based on the given condition.

    :param escape: Boolean. If using html renderer, escape html.
    :param renderer: renderer instance or string of ``html`` and ``ast``.
    :param plugins: List of plugins, string or callable.

    This method is used when you want to re-use a Markdown instance::

        markdown = create_markdown(
            escape=False,
            renderer='html',
            plugins=['url', 'strikethrough', 'footnote', 'table'],
        )
        # re-use markdown function
        markdown('.... your text ...')
    """
    if renderer is None or renderer == 'html':
        renderer = HTMLRenderer(escape=escape)
    elif renderer == 'ast':
        renderer = AstRenderer()

    if plugins:
        _plugins = []
        for p in plugins:
            if isinstance(p, str):
                _plugins.append(PLUGINS[p])
            else:
                _plugins.append(p)
        plugins = _plugins
    return Markdown(renderer, plugins=plugins)


html = create_markdown(
    escape=False,
    renderer='html',
    plugins=['strikethrough', 'footnote', 'table'],
)


def markdown(text, escape=True, renderer=None, plugins=None):
    md = create_markdown(escape, renderer, plugins)
    return md(text)


__all__ = [
    'Markdown', 'AstRenderer', 'HTMLRenderer',
    'BlockParser', 'InlineParser',
    'escape', 'escape_url', 'escape_html', 'unikey',
    'html', 'create_markdown', 'markdown',
]

__version__ = '2.0.0'
