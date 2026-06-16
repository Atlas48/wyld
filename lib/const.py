from enum import Enum
from pathlib import Path

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
