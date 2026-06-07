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
	src=build/i.with_suffix('.html')
	src.write_text(templ.basic.render(content=i.read_text()))

for d in COLLECTIONS:
	src=CARD_DIR/d
	(build/src).mkdir(exist_ok=True,parents=True)
	for i in src.iterdir():
		if not i.name.endswith('.md'):
			continue
		dest=build/i.with_suffix('.svg')
		if dest.exists():
			ss=i.stat()
			ds=dest.stat()
			if ss.st_mtime<ds.st_time or ss.st_size!=ds.st_size:
				del ds
				del ss
				continue
		cc=frontmatter_loads(i.read_text())
		if 'img' in cc.metadata and cc.metadata['img'] is not None and ('datauri' not in cc.metadata or cc.metadata['datauri'] is None):
			cc.metadata['datauri']=datauri(cc.metadata['img'])
		dest.write_text(templ.card.render(**cc.metadata,content=cc.content,type=CardType[d.capitalize()],CardType=CardType))
