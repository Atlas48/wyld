from pathlib import Path
from frontmatter import loads as frontmatter_loads
from libconst import *

for d in COLLECTIONS:
	src=CARD_DIR/d
	for i in src.iterdir():
		if not i.name.endswith('.md'):
			continue
		cc=frontmatter_loads(i.read_text())
		if 'img' not in cc.metadata:
			print('X',i.relative_to(CARD_DIR.parent))
		elif cc.metadata['img'] is None:
			print('O',i.relative_to(CARD_DIR.parent))
		else:
			print('-',i.relative_to(CARD_DIR.parent))
