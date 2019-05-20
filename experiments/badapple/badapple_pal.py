import pyb
import framebuf

#pyb.freq(84000000, 84000000, 42000000, 84000000)

@micropython.native
def intro(step=1):
    _bksize = 80*128
    tft = pyb.SCREEN()
    fbuf = bytearray(_bksize)
    fb = framebuf.FrameBuffer(fbuf, 160, 128, framebuf.PAL16, 160, framebuf.PAL16_ADAPTIVE_GS)  
    r = range(0, 6535, step)
    blit = tft.show

    with open("anim/badapple_PAL16.dat", "rb") as f:
        for nb in r:
            f.readinto(fbuf)
            blit(fb)

# step: how many images to skip between 2 frames
intro(step=1)
