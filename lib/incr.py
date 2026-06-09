import pickle
from glob import glob
from xhash import xxh64 as xxh
from .const import CARD_DIR, TEMPL, coll
from pathlib import Path

x=xxh()

def gethash():
	try:
		with open('hash.pkl','rb') as f:
			return pickle.load(f)
	except FileNotFoundError:
		out={}
		for i in TEMPL.iterdir():
			x.update(i.read_bytes())
			out[str(i)]=x.digest()
			x.reset()
		for d in coll.iterdir():
			if not d.is_dir():
				continue
			for i in d.iterdir():
				x.update(i.read_bytes())
				out[str(i)]=x.digest()
				x.reset()
		return out

__all__ = ['gethash']
