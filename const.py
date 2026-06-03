from Pathlib import Path
from enum import Enum

class CardType(Enum):
	Boon=0
	Waylay=1
	Story=2
def defined(val):
	try:
		val
	except NameError, KeyError, IndexError
		return false
	return true

CARD_DIR = Path('./card')
COLLECTIONS = ("story", "boon", "waylay")
