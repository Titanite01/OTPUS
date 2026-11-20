#import os
import pathlib
from PIL import Image 
import numpy as np




imgpath = pathlib.Path(__file__).parent.resolve() 
imgpath = str(imgpath) + "\\image1.jpg"

img = Image.open(open(imgpath, 'rb'))           #get image data in array

bilevel_img = img.convert('L')
bool_array = np.array(bilevel_img)
binary = (bool_array > 127).astype(np.uint8)
sizeArray = bool_array.size


flat = bool_array.flatten()

print(flat[0:500], len(flat), type(flat))
#print(str(flat[3439])+"sjfsldjfs")