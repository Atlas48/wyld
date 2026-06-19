from enum import Enum
from pathlib import Path

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2

root=Path('.')
build=Path('build')
tempf=Path('templ')
CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
coll=[CARD_DIR/c for c in COLLECTIONS]
