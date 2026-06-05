from pathlib import Path
from enum import Enum
from base64 import urlsafe_b64encode as b64
from mimetypes import guess_type

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2
def datauri(p:str):
	pp=CARD_DIR/"img"/Path(p)
	t=guess_type(p)
	if t=="image/svg+xml":
		return "data:image/svg+xml,"+urlencode(pp.read_text())
	else:
		return "data:%s;base4,%s"%(t,b64(pp.read_bytes()))

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
