## Supported Formats
 - [x] BMP from Meowbit official fork
   - 24bits only
   - no compression
 - [x] GIF - from Meowbit official fork
   - animated only
 - [x] JPEG - modified [picojpeg](https://github.com/PrometheanDesign/picojpeg/tree/master/test)
   - no progressive JPEG
 - [ ] Raw 256, 8bpp indexed palette mode
   - [x] no palette
   - [ ] with custom palette
 - [ ] Raw 16, 4bpp indexed palette 
   - [x] no palette
   - [ ] with custom palette

## API

 - `Image.loadbmp(filename, [x, y])`
 - `Image.loadgif(filename, [x, y, callback])`
 - `Image.loadjpeg(filename)`
 - `Image.loadp16(filename)`
 - `Image.loadp256(filename)`

Example:
````python
import pyb
import framebuf
import image

fbuf = bytearray(160*128*2)
tft = pyb.SCREEN()
fb = framebuf.FrameBuffer(fbuf, 160, 128, framebuf.RGB565, 160)

img = image.Image(fb)
img.loadjpeg("images/test.jpg")
tft.show(fb)
````

## Performance

Those number are the processing average time including
- read a file from the SD card
- process the file
- fill the framebuffer's `bytearray`

Blitting to screen is not included.

| Decoder | Format | CPU | AHB | APB1 | APB2 | Average time in ms | Freq improvement |
|:-------:|:------:|:---:|:---:|:----:|:----:|:------------------:|:----------------:|
|   BMP   | RGB565 |  56 |  56 |  14  |  28  |        72.75       |                  |
|   BMP   | RGB565 |  84 |  84 |  42  |  84  |        51.89       |      -28.68%     |
|   JPEG  | RGB565 |  56 |  56 |  14  |  28  |       224.88       |                  |
|   JPEG  | RGB565 |  84 |  84 |  42  |  84  |       153.26       |      -31.85%     |
|   P16   |  PAL16 |  56 |  56 |  14  |  28  |        3.71        |                  |
|   P16   |  PAL16 |  84 |  84 |  42  |  84  |        3.04        |      -18.10%     |
|  P16+Py |  PAL16 |  56 |  56 |  14  |  28  |        4.37        |                  |
|  P16+Py |  PAL16 |  84 |  84 |  42  |  84  |        3.47        |      -20.58%     |
|   P256  | PAL256 |  56 |  56 |  14  |  28  |        5.05        |                  |
|   P256  | PAL256 |  84 |  84 |  42  |  84  |        3.91        |      -22.47%     |
| P256+Py | PAL256 |  56 |  56 |  14  |  28  |        5.68        |                  |
| P256+Py | PAL256 |  84 |  84 |  42  |  84  |        4.34        |      -23.64%     |

Notes:
 - P16/P256+Py means it doesn't use the Module, the reading of the file content was done in Python using `f.readinto(fbuf)`. That's to see how managing the file in C is faster (around +15% faster)

````python
import pyb
import framebuf

fbuf = bytearray(80*128)
tft = pyb.SCREEN()
fb = framebuf.FrameBuffer(fbuf, 160, 128, framebuf.PAL16, 160, framebuf.PAL16_C64)

with open("images/test.p16", "rb") as f:
    f.readinto(fbuf)
    tft.show(fb)
````


Reminder: 
 - a frame at 60Hz = 16.66ms / 50Hz = 20ms
 - 25 Fps = 40ms per frame max
