from pathlib import Path
from enum import Enum
from base64 import b64encode as b64
from mimetypes import guess_type
from urllib.parse import quote as urlencode

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
