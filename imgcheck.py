from pathlib import Path
from frontmatter import loads as frontmatter_loads
from const import *

for d in COLLECTIONS:
	src=CARD_DIR/d
	for i in src.iterdir():
		if not i.name.endswith('.md'):
			continue
		cc=frontmatter_loads(i.read_text())
		if 'img' not in cc.metadata:
			print('Image field does not exist on',i.name)
		elif cc.metadata['img'] is None:
			print('Image field is null on',i.name)
