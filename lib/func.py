from pathlib import Path

def datauri(p:str):
	pp=Path("img")/Path(p)
	t=guess_type(p)[0]
	if not pp.exists():
		with open("img/test.png","rb") as f:
			return "data:image/png;base4,"+b64(f.read()).decode()
	if t is None:
		raise TypeError('mimetypes could not guess type of %s'%p)
	if t=="image/svg+xml":
		return "data:image/svg+xml,"+urlencode(pp.read_text())
	else:
		return "data:%s;base64,%s"%(t,b64(pp.read_bytes()).decode())
def slugify(title: str) -> str:
	return re.sub(r"\s+", "-", re.sub(r'[!"£$%^*()\[\];\'#:@~`<>?,./|\\]', "", title.lower()).strip())
