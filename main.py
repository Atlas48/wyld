# Card renderer
from types import SimpleNamespace as Namespace
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from frontmatter import loads as frontmatter_loads
from markdown import markdown
from const import *

root=Path('.')
build=Path('build')

if not build.exists():
	try:
		build.mkdir()
	except FileExistsError:
		from sys import stderr,exit
		print("Well gee, tell the file named build to MOVE ITS ASS. IT'S BLOCKING THE WAY OF A DIRECTORY.", file=stderr)
		exit(1)

jenv=Environment(loader=FileSystemLoader('templ'), trim_blocks=True, lstrip_blocks=True)
jenv.filters['markdown']=markdown
def warn(i):
	raise Warn(i)
jenv.globals['warn']=warn

templ=Namespace(card=jenv.get_template('card.svg.j2'),basic=jenv.get_template('basic.html.j2'))

for i in root.glob('*.md'):
	cur=build/i.with_suffix('.html')
	cur.write_text(templ.basic.render(content=i.read_text()))

for d in COLLECTIONS:
	cur=CARD_DIR/d
	(build/cur).mkdir(exist_ok=True,parents=True)
	for i in cur.iterdir():
		if not i.name.endswith('.md'):
			continue
		cc=frontmatter_loads(i.read_text())
		if 'img' in cc.metadata and cc.metadata['img'] is not None:
			cc.metadata['datauri']=datauri(cc.metadata['img'])
		else:
			print('Image not present for',i)
		(build/i.with_suffix('.svg')).write_text(templ.card.render(**cc.metadata,content=cc.content,type=CardType[d.capitalize()],CardType=CardType))
