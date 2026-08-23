#!/usr/bin/env python

from pathlib import Path
from lib.const import COLLECTIONS,CARD_DIR

total={
	'story': 55,
	'waylay': 0x20,
	'boon': 0x20,
	'summon': 0x0A
}

coll=map(lambda i: CARD_DIR/i,COLLECTIONS)

for d in coll:
	c=0
	for i in d.iterdir():
		if i.name.startswith('test') or not i.name.endswith('.md'):
			continue
		c+=1
	if d.name in total:
		print(d.name,c,'/',total[d.name],"(%.2f%%)"%((c/total[d.name])*100))
	else:
		print(d.name,c)
