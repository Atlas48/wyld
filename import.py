#!/usr/bin/env python3
from sys import stderr, argv
try:
	ctype = argv[1]
	files = argv[2:]
except IndexError:
	print('%s: [waylay|boon|story] <import files>' % argv[0], file=stderr)
	exit()

from subprocess import Popen, PIPE
from pathlib import Path
from lib.func import slugify

template = '''---
title: %s
layout: card.pug
special: false
xp: 0
---

%s
'''

for fn in files:
	p = Popen(["awk", 'BEGIN{ORS=FS} $1=="#" {for(i=2;i<NR;i++) print $i;printf "\\n";}', fn], stdout=PIPE, text=True)

	for title in p.stdout:
		title = title.rstrip('\n')
		if not title:
			continue

		if len(title) > 255:
			print(f"Skipping {fn}: title too long ({len(title)} chars).", file=stderr)
			continue

		out_path = Path("card") / ctype / f"{slugify(title)}.md"

		if out_path.exists():
			print(f"Skipping {fn}: {out_path} already exists.", file=stderr)
			continue

		with open(out_path, 'w') as out_f:
			out_f.write(template % (title, ''))

		print(f"Generated {out_path}")
