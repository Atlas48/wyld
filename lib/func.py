import re
from pathlib import Path
from mimetypes import guess_type
from base64 import b64encode as b64
from urllib.parse import quote as urlencode

def datauri(p:str):
	pp=Path("img")/Path(p)
	t=guess_type(p)[0]
	if not pp.exists():
		with open("img/test.png","rb") as f:
			return "data:image/png;base64,"+b64(f.read()).decode()
	if t is None:
		raise TypeError('mimetypes could not guess type of %s'%p)
	if t=="image/svg+xml":
		return "data:image/svg+xml,"+urlencode(pp.read_text())
	else:
		return "data:%s;base64,%s"%(t,b64(pp.read_bytes()).decode())
def slugify(title: str) -> str:
	return re.sub(r"\s+", "-", re.sub(r'[!"£$%^*()\[\];\'#:@~`<>?,./|\\]', "", title.lower()).strip())
