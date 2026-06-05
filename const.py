from pathlib import Path
from enum import Enum
from base64 import b64encode as b64
from mimetypes import guess_type
from urllib.parse import quote as urlencode

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2
class Warn(Exception):
	pass
def datauri(p:str):
	pp=CARD_DIR/"img"/Path(p)
	t=guess_type(p)[0]
	if t is None:
		raise TypeError('mimetypes could not guess type of %s'%p)
	if t=="image/svg+xml":
		return "data:image/svg+xml,"+urlencode(pp.read_text())
	else:
		return "data:%s;base64,%s"%(t,b64(pp.read_bytes()).decode())

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
