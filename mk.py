#!/usr/bin/env python3
# Card renderer
import argparse
from copy import deepcopy
from pathlib import Path
from pickle import dump as pickle_dump
from frontmatter import loads as frontmatter_loads
from lib.const import *
from lib.jenv import jenv, templ
from lib.incr import *
from lib.func import datauri
from xxhash import xxh64 as xxh

x=xxh()
ap=argparse.ArgumentParser()
ap.add_argument('-a','--all',action='store_true')
arg=ap.parse_args()
fhash=gethash()
shash=deepcopy(fhash)

if not build.exists():
	try:
		build.mkdir()
	except FileExistsError:
		from sys import stderr,exit
		print("Well gee, tell the file named build to MOVE ITS ASS. IT'S BLOCKING THE WAY OF A DIRECTORY.", file=stderr)
		exit(1)

if fhash=={} or arg.all:
	print('Rebuilding...')
	fhash=mkhash()

print('Checking templates')
cardsame=templsame('card.svg.j2',fhash)
basesame=templsame('basic.html.j2',fhash)

for i in root.glob('*.md'):
	ch=qxh(i.read_bytes())
	if not arg.all and basesame and fhash.get(str(i))==ch:
		continue
	src=build/i.with_suffix('.html')
	src.write_text(templ.basic.render(content=i.read_text()))
	fhash[str(i)]=ch

for d in coll:
	(build/d).mkdir(exist_ok=True,parents=True)
	for i in d.iterdir():
		if not i.name.endswith('.md'):
			continue
		ch=qxh(i.read_bytes())
		if not arg.all and cardsame and fhash.get(str(i))==ch:
			continue #as well
		dest=build/d/i.with_suffix('.svg').name
		cc=frontmatter_loads(i.read_text())
		if 'img' in cc.metadata and cc.metadata['img'] is not None and ('datauri' not in cc.metadata or cc.metadata['datauri'] is None):
			cc.metadata['datauri']=datauri(cc.metadata['img'])
		if 'txtsize' not in cc.metadata or cc.metadata['txtsize'] is None:
			cc.metadata['txtsize']=0
		if 'ttlsize' not in cc.metadata or cc.metadata['ttlsize'] is None:
			cc.metadata['ttlsize']=0
		dest.write_text(templ.card.render(**cc.metadata,content=cc.content,type=CardType[d.name.capitalize()],CardType=CardType))
		fhash[str(i)]=ch
		print(i.name,dest.name,sep=" -> ")
if shash!=fhash:
	with open('hash.pkl','wb') as f:
		pickle_dump(fhash,f)
else:
	print("Nothing to compile.")
