import pickle
from xxhash import xxh64 as xxh
from .const import *

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
	except (EOFError, pickle.UnpicklingError):
		from os import remove as rm
		from sys import stderr
		print("hash.pkl is corrupt, cleaning.",file=stderr)
		rm('hash.pkl')
		return {}
def mkhash():
	out={}
	for i in tempf.iterdir():
		out[str(i)]=qxh(i.read_bytes())
	return out
def templsame(p,fhash):
	c=tempf/p
	h=qxh(c.read_bytes())
	out=fhash.get(str(c))!=h
	if out:
		fhash[str(c)]=h
	return not out

__all__ = ['gethash','qxh','mkhash','templsame']
