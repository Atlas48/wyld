from sys import stderr, argv,
from collections import namedtuple
from math import floor
from PIL import Image, UnidentifiedImageError

HeightWidth=namedtuple('HeightWidth',['h','w'])

if len(argv)>2:
	print("Nothing to process.",file=stderr)
	exit(1)

for i in argv:
	try:
		with Image.open(i) as im:
			#aww yeah name that tuple.
			#its size B)
			hw=HeightWidth(im.size)
	except FileNotFoundError:
		print(f"Listed file, {i}, does not exist.",file=stderr)
		continue
	except UnidentifiedImageError as e:
		print(f"Listed file, {i} is in an unknown format: {e}",file=stderr)
		continue
	except ValueError as e: #can't happen
		print("Somehow managed to get a ValueError. Exiting immediately.",file=stderr)
		print(e,file=stderr)
		exit(1)
	h=hw.w*5
	w=hw.h*7
	if hw.h==120 and hw.w==168:
		print(i,"doesn't need changing")
	elif h<=w:
		print(i,*hw,hw.w,w//7,sep="\t")
	else:
		print(i,*hw,hw.h,h//5,sep="\t")
