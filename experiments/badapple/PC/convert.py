import PIL
from PIL import Image

import glob
from glob import iglob

import hashlib
import pickle

import ntpath
import os
import shutil
import math

ORIGINAL = "resized/xnview/"

#RESIZED = "resized/raw/"
#TGT_COLOR_MODE = 'RGB565'

RESIZED = "resized/pal16"
TGT_COLOR_MODE = 'PAL16'

#ORIGINAL = "resized/test/"
#RESIZED = "resized/test/"
#TGT_COLOR_MODE = 'PAL16'

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def load_palette(filename):  
    with open(filename, "r") as fin:
        #  headers
        id = fin.readline()
        version = fin.readline()
        size = fin.readline()

        if "JASC-PAL" not in id:
            print("Wrong file format {}".format(id))
            exit(-1)
        
        rgb3 = []
        for i in range(0, 16):
            colors = fin.readline().rstrip("\n\r").split(" ")
            rgb3.append([int(colors[0]), int(colors[1]), int(colors[2]) ])

    return rgb3, hashlib.md5(pickle.dumps(rgb3)).hexdigest()

def remap(buffer, pal_src, pal_dest):
    remap_list = []
    for src_rgb_color in pal_src:
        sel = 999999999
        for num, dst_rgb_color in enumerate(pal_dest):
            dist = math.sqrt((dst_rgb_color[0] - src_rgb_color[0])**2 + (dst_rgb_color[1]  - src_rgb_color[1])**2 + (dst_rgb_color[2] - src_rgb_color[2])**2 )
            if dist < sel:
                idx = num
                sel = dist
        remap_list.append(idx)

    #print("remapping table computed")
    #for i in range(0, 16):
    #    print(i, pal_src[i], 'is mapped to index', remap_list[i], 'which is', pal_dest[remap_list[i]])

    buffer2 = bytearray()
    for old_col in buffer:
        new_col = remap_list[old_col]
        buffer2.append(new_col)
        #print(old_col, new_col)

    return buffer2

def rgb_hex565(red, green, blue):
    # take in the red, green and blue values (0-255) as 8 bit values and then combine
    # and shift them to make them a 16 bit hex value in 565 format. 
    return (int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31))

# -----------------------------------------------------------------------------------------------

pal_ref, pal_ref_md5 = load_palette("palette_16gs_ref.pal")

files = sorted(glob.glob(ORIGINAL + "*.png"))
for filename in files:

    print("Converting ", filename)
    img = Image.open(filename)

    if img.size[0] != 160 or img.size[1] != 128:
        print("Resize image")
        img = img.resize((160, 128), PIL.Image.LANCZOS)

    data = bytearray()
    if TGT_COLOR_MODE == 'RGB565':
        img = img.convert(mode='RGB')
        raw = list(img.getdata())

        #print("res 160x128={}, raw length: {}".format(160*128, len(raw)))
        for triple in raw:
            r = triple[0]
            g = triple[1]
            b = triple[2]

            pixel = rgb_hex565(r, g, b).to_bytes(2, byteorder="big")      
            data.append(pixel[0])
            data.append(pixel[1])

    elif TGT_COLOR_MODE == 'PAL16':
        
        #import hitherdither
        #import dither
        #palette = hitherdither.palette.Palette(pal_img.getpalette())
        #img_dithered = hitherdither.diffusion.error_diffusion_dithering(img, palette=palette, method='floyd-steinberg', order=2)
        #dither.Dither(path=filename, output="toto.png")

        #img = img.convert(mode='P', colors=16, palette=Image.ADAPTIVE)
        #img.save(os.path.splitext(RESIZED + '/' + ntpath.basename(filename))[0] + '_16.png', format="PNG", bits=4)
        #print("res 160x128={}, raw length: {}".format(160*128, len(raw)))     
      
        # for pure black image, palette is wrong
        pal = img.getpalette()

        pal_rgb = list(chunks(pal, 3))
        pal_rgb_md5 = hashlib.md5(pickle.dumps(pal_rgb)).hexdigest()

        # get pixels list
        raw = list(img.getdata())  

        if pal_rgb_md5 != pal_ref_md5:
            print("not a known palette, trying to remap...")
            raw = remap(raw, pal_rgb, pal_ref)

        for i in range(0, len(raw), 2):
            b1 = (raw[i+0] & 0x0f) << 4
            b2 = (raw[i+1] & 0x0f)
            b3 = (b1 | b2)            
            data.append(b3)
            #print("b1: {:02x} b2: {:02x} b3: {:02x} data: {}".format(b1, b2, b3, data)) 

    # save raw
    with open(os.path.splitext(RESIZED + '/' + ntpath.basename(filename))[0] + '.raw','wb') as rawfile:
        rawfile.write(data)

# concatenate raw files
dest = open('badapple_' + TGT_COLOR_MODE+ '.dat', 'wb')
for filename in sorted(iglob(os.path.join(RESIZED, '*.raw'))):
    print("Adding: ", filename)
    shutil.copyfileobj(open(filename, 'rb'), dest)
dest.close() 
