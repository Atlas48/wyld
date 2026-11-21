#!/usr/bin/env python3
from sys import stderr, argv
def nope():
	from sys import exit
	print('%s: [waylay|boon|story|summon] <import files>' % argv[0], file=stderr)
	exit()
try:
	ctype = argv[1]
	files = argv[2:]
except IndexError:
	nope()
if ctype not in ("waylay","boon","story","summon"):
	nope()
del nope

from subprocess import Popen, PIPE
from pathlib import Path
from lib.func import slugify
import tomlkit

for fn in files:
	p = Popen(["awk", 'BEGIN{ORS=FS} $1=="#"&&NF>1 {for(i=2;i<=NF;i++) print $i;printf "\\n";}', fn], stdout=PIPE, text=True)

	for title in p.stdout:
		title = title.strip()
		doc=tomlkit.document()
		if not title:
			continue
		if len(title) > 255:
			print(f"Skipping {fn}: title too long ({len(title)} chars).", file=stderr)
			continue
		out_path = Path("card") / ctype / f"{slugify(title)}.toml"
		if out_path.exists():
			print(f"Skipping {fn}: {out_path} already exists.", file=stderr)
			continue
		doc["title"]=title
		doc["xp"]=doc["txtsize"]=doc["ttlsize"]=0
		doc["special"]=False
		doc.add("content", tomlkit.string("",multiline=True))
		with open(out_path, 'w', encoding='utf-8') as out_f:
			out_f.write(tomlkit.dumps(doc))
		print(f"Generated {out_path}")
