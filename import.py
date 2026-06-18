#!/usr/bin/env python3
from sys import stderr, argv
try:
    ctype = argv[1]
    files = argv[2:]
except IndexError:
    print('%s: [waylay|boon|story] <import files>' % argv[0], file=stderr)
    exit()

import re
from pathlib import Path
from lib.func import slugify
from frontmatter import Post, dump as frontmatter_dump

for fn in files:
    with open(fn, 'r') as f:
        title = None
        content_lines = []
        in_content = False

        for line in f:
            if title is None and re.match(r'^# ', line):
                title = line[2:].strip()
                in_content = True
                continue
            if in_content:
                content_lines.append(line)

        if title is None:
            print(f"Skipping {fn}: no title line starting with '# ' found.", file=stderr)
            continue

        if len(title) > 255:
            print(f"Skipping {fn}: title too long ({len(title)} chars).", file=stderr)
            continue

        out_path = Path("card") / ctype / f"{slugify(title)}.txt"

        if out_path.exists():
            print(f"Skipping {fn}: {out_path} already exists.", file=stderr)
            continue

        post = Post(
            content=''.join(content_lines).strip(),
            title=title,
            layout='card.pug',
            special=False,
            xp=0
        )

        with open(out_path, 'w') as out_f:
            frontmatter_dump(post, out_f)

        print(f"Generated {out_path}")
