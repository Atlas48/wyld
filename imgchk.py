#!/usr/bin/python
#see also: util/imgcount.awk
from os.path import isfile
from pathlib import Path
from tomlkit import loads as frontmatter_loads
from lib.const import *

for d in COLLECTIONS:
	src=CARD_DIR/d
	for i in src.iterdir():
		if not i.name.endswith('.toml'):
			continue
		cc=frontmatter_loads(i.read_text())
		if 'img' not in cc:
			print('X',*i.relative_to(CARD_DIR).parts)
		elif cc['img'] is None or cc['img']=="":
			print('O',*i.relative_to(CARD_DIR).parts)
		elif not isfile("img/"+cc['img']):
			print('~',*i.relative_to(CARD_DIR).parts)
		else:
			print('-',*i.relative_to(CARD_DIR).parts)
