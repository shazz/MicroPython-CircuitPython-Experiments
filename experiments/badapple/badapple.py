import pyb
import framebuf

@micropython.native
def intro(step):
    _bksize = 160*128*2
    tft = pyb.SCREEN()
    fbuf = bytearray(_bksize)
    fb = framebuf.FrameBuffer(fbuf, 160, 128, framebuf.RGB565)  
    r = range(0, 6535, step)
    blit = tft.show

    with open("badapple.dat", "rb") as f:
        for nb in r:
            f.readinto(fbuf)
            blit(fb)

# step: how many images to skip between 2 frames
intro(step=1)

