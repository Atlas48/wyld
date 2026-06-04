from pathlib import Path
from enum import Enum

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
