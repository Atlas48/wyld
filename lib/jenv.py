from types import SimpleNamespace as Namespace
from functools import partial
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
class Warn(Exception):
	pass
def warn(i):
	raise Warn(i)
jenv=Environment(loader=FileSystemLoader('templ'), trim_blocks=True, lstrip_blocks=True)
jenv.filters['markdown']=partial(markdown,extensions=['nl2br'])
jenv.globals['warn']=warn

templ=Namespace(card=jenv.get_template('card.svg.j2'),basic=jenv.get_template('basic.html.j2'))

__all__ = ['jenv','templ']
