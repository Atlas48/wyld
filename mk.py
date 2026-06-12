# Card renderer
from pathlib import Path
from frontmatter import loads as frontmatter_loads
from lib.const import *
from lib.jenv import jenv, templ 

root=Path('.')
build=Path('build')

if not build.exists():
	try:
		build.mkdir()
	except FileExistsError:
		from sys import stderr,exit
		print("Well gee, tell the file named build to MOVE ITS ASS. IT'S BLOCKING THE WAY OF A DIRECTORY.", file=stderr)
		exit(1)


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
		cc=frontmatter_loads(i.read_text())
		if 'img' in cc.metadata and cc.metadata['img'] is not None and ('datauri' not in cc.metadata or cc.metadata['datauri'] is None):
			cc.metadata['datauri']=datauri(cc.metadata['img'])
		if 'txtsize' not in cc.metadata or cc.metadata['txtsize'] is None:
			cc.metadata['txtsize']=0
		if 'ttlsize' not in cc.metadata or cc.metadata['ttlsize'] is None:
			cc.metadata['ttlsize']=0
		dest.write_text(templ.card.render(**cc.metadata,content=cc.content,type=CardType[d.capitalize()],CardType=CardType))
		print(i.name,dest.name,sep=" -> ")
