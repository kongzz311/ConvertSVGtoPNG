import os
from cairosvg import svg2png

path = input('Input the path of the svg ')
dirpath = os.path.dirname(path)
filename = os.path.basename(path).split('.')[0]+".png"

svg2png(url=path, write_to=dirpath + '/' + filename)
