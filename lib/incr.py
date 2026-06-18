import pickle
from xhash import xxh64 as xxh
from .const import *
from pathlib import Path

x=xxh()

def qxh(dat):
	x.update(dat)
	out=x.digest()
	x.reset()
	return out

def gethash():
	try:
		with open('hash.pkl','rb') as f:
			return pickle.load(f)
	except FileNotFoundError:
		return {}
def mkhash():
	out={}
	for i in tempf.iterdir():
		out[str(i)]=qxh(i.read_bytes())
	for d in coll.iterdir():
		if not d.is_dir():
			continue
		for i in d.iterdir():
			x.update(i.read_bytes())
			out[str(i)]=x.digest()
			x.reset()
	return out
def templupdated(p,):
	c=temf/p
	return fhash.get(str(c))!=qxh(c.read_bytes())

__all__ = ['gethash','qxh','mkhash','templupdated']
