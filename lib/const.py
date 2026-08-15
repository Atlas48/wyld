from enum import Enum
from pathlib import Path

class CardType(Enum):
	Boon=0
	Summon=1
	Waylay=2
	Story=3

root=Path('.')
build=Path('build')
tempf=Path('templ')
CARD_DIR = Path('./card')
COLLECTIONS = ("boon", "summon", "story", "waylay")
coll=[CARD_DIR/c for c in COLLECTIONS]
