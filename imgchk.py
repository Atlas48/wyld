#!/usr/bin/python
from os.path import isfile
from pathlib import Path
from frontmatter import loads as frontmatter_loads
from lib.const import *

for d in COLLECTIONS:
	src=CARD_DIR/d
	for i in src.iterdir():
		if not i.name.endswith('.md'):
			continue
		cc=frontmatter_loads(i.read_text())
		if 'img' not in cc.metadata:
			print('X',*i.relative_to(CARD_DIR).parts)
		elif cc.metadata['img'] is None or cc.metadata['img']=="":
			print('O',*i.relative_to(CARD_DIR).parts)
		elif not isfile("img/"+cc.metadata['img']):
			print('~',*i.relative_to(CARD_DIR).parts)
		else:
			print('-',*i.relative_to(CARD_DIR).parts)
