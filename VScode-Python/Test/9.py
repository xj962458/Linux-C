from numpy.lib.type_check import imag
import requests
from PIL import Image
import numpy as np

r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1607964223342&di=ff99345abf401179205f0125d116d772&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20190217%2F74b027cd90f24603943bad768f65247d.jpeg',timeout=30)
with open('./test.jpg','wb') as f:
    f.write(r.content)

im0=np.array(Image.open('./test.jpg').convert('L'))
im1=255-im0
im2=(100/255)*im0+150
im3=255*(im1/255)**2
for i in [im0,im1,im2,im3]:
    pil_im=Image.fromarray(np.uint(i))
    pil_im.show()



