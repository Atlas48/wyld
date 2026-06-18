#!/usr/bin/env python

from pathlib import Path
from lib.const import COLLECTIONS,CARD_DIR

coll=map(lambda i: CARD_DIR/i,COLLECTIONS)

for d in coll:
	c=0
	for i in d.iterdir():
		if i.name.startswith('test') or not i.name.endswith('.md'):
			continue
		c+=1
	print(d.name,c)
