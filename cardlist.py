from pathlib import Path
from sys import stderr
from functools import partial

root=Path('build')
scan=root/'card'
f=(root/"index.html").open('w')
head="""<!DOCTYPE html>
<html>
<head>
<title>Template List</title>
</head>
<body>
"""
foot="</body>\n</html>"

def wrap(s1,s2):
	return f"<{s1}>{s2}</{s1}>"
def img(s):
	return '<img src="%s" />'%s
h1=partial(wrap,"h1")
p=partial(wrap,"p")
pr=partial(print,file=f)

if not root.exists():
	print("Can't run yet, need the build dir to exist.",file=stderr)
	exit(2)
if not root.is_dir():
	print("Despite prior warnings, something is blocking the way of the build dir.", file=stderr)
	exit(2)

f.write(head)
for i in scan.iterdir():
	if i.name.endswith('html') or not i.is_dir():
		continue
	print(i)
	pr(h1(i.name.capitalize()))
	for ii in i.iterdir():
		print(ii)
		pr(p(img(ii.relative_to(root))))
f.write(foot)
f.close()
