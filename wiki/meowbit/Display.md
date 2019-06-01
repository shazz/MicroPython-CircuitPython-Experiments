# WARNING: this is not official information, only in progress retro-engineering ##

## Hardware

It looks like the Meowbit uses a [ST7735](https://www.displayfuture.com/Display/datasheet/controller/ST7735.pdf) TFT controller:
* using the SPI bus (SPI2 spi2 pin pb12~15) at 22MHz, check pins `SPI4W` = 0 or 1 to VDDI for 3 or 4 SPI lines, I guess 4.
* in mode 160x128 (pins `GM0`, `GM1`, `GM2`) to `b011`, full display (`ST7735_NORON`)
* in color mode `ST7735_COLMOD 0x0C`: `b101` (16 bits per pixel, 565) 
* Gamma parameters are in the bootloader: `ST7735_GMCTRP1` and `ST7735_GMCTRN1`

### Init

````
static const uint8_t initCmds[] = {
    ST7735_SWRESET,   DELAY,  //  1: Software reset, 0 args, w/delay
      120,                    //     150 ms delay
    ST7735_SLPOUT ,   DELAY,  //  2: Out of sleep mode, 0 args, w/delay
      120,                    //     500 ms delay
    ST7735_INVOFF , 0      ,  // 13: Don't invert display, no args, no delay
    ST7735_INVCTR , 1      ,  // inverse, riven
      0x03,
    ST7735_COLMOD , 1      ,  // 15: set color mode, 1 arg, no delay:
      0x05,                  //     16-bit color
    ST7735_GMCTRP1, 16      , //  1: Magical unicorn dust, 16 args, no delay:
      0x02, 0x1c, 0x07, 0x12,
      0x37, 0x32, 0x29, 0x2d,
      0x29, 0x25, 0x2B, 0x39,
      0x00, 0x01, 0x03, 0x10,
    ST7735_GMCTRN1, 16      , //  2: Sparkles and rainbows, 16 args, no delay:
      0x03, 0x1d, 0x07, 0x06,
      0x2E, 0x2C, 0x29, 0x2D,
      0x2E, 0x2E, 0x37, 0x3F,
      0x00, 0x00, 0x02, 0x10,
    ST7735_NORON  ,    DELAY, //  3: Normal display on, no args, w/delay
      10,                     //     10 ms delay
    ST7735_DISPON ,    DELAY, //  4: Main screen turn on, no args w/delay
      10,
    0, 0 // END
};
````

### Display Settings

* `FRMCTR1 (B1h)` Frame Rate Control: 
````
RTNA=0
FPA=0b110
BPA=0b11

FR = fosc/((RTNA + 20) x (LINE + FPA + BPA))  
with fosc=333KHz and LINE=???
````

* `MADCTL (36h)` Memory Data Access Control:
````
0x40 (0b01000000)
MY=0 (T->B) 
MX=1 (R->L) 
MV=0 (nor) 
ML=0 (refresh T->B) 
RGB=0 (RGB) 
MH=0 (LCD Ref L->R) 
Unused=00
````

* `RASET (2Bh)` Row Address Set: 0, 0, 0, 159
* `CASET (2Ah)` Column Address Set: 0, 0, 0, 127

### Synchronization

It looks like the synchronization between the TFT Controller and the MPU can be achieved usign the `Tearing Effect Line (TEON 0x35)` signal.

Accordingly the Pin TE has to be connected to the MPU. Is it the case ? Which pin of the MPU ? 

````
Set TEON mode (set off at power)
D/CX=1 + WRX up + RDC=1
bit 0 (TELOM) = 0 => V-Blank is generated
bit 0 (TELOM) = 1 => V-Blank and H-Blank are generated
````

TEON value can be accessed using 
````
RDDST (09h): Read Display Status 
To check, looks like the bit 1 of the 4th byte should be set to 1

RDDSM (0Eh): Read Display Signal Mode 

````


## Firmware

Bootloader Flasher Source-code: [screen.c](https://github.com/KittenBot/uf2-meowbit/blob/fat/screen.c)


### 16 colors palette mode

This is a software mode, means translated by code into the 16-bit color mode. The palette is hardcoded.
Basically, the code 

1. parses each byte of the bytearray (containing the palette index between 0 and 15)
1. gets the equivalent 16 bit value (based on the palette table)
1. formats the value to be compatible with the SPI transfer (high byte then low byte)
1. sends each pixel value value, one by one thru SPI using the command `ST7735_RAMWR` (`0x2C`, Memory Write) so 160x128 times

````
void draw_screen() {
    cmdBuf[0] = ST7735_RAMWR;
    sendCmd(cmdBuf, 1);

    SET_DC(1);
    SET_CS(0);

    uint8_t *p = fb;
    for (int i = 0; i < DISPLAY_WIDTH; ++i) {
        for (int j = 0; j < DISPLAY_HEIGHT; ++j) {
            uint16_t color = palette[*p++ & 0xf];
            uint8_t cc[] = {color >> 8, color & 0xff};
            spi_transfer(cc, 2);
        }
    }

    SET_CS(1);
}
````

````
#define COL0(r, g, b) ((((r) >> 3) << 11) | (((g) >> 2) << 5) | ((b) >> 3))
#define COL(c) COL0((c >> 16) & 0xff, (c >> 8) & 0xff, c & 0xff)

const uint16_t palette[] = {
    COL(0x000000), // 0
    COL(0xffffff), // 1
    COL(0xff2121), // 2
    COL(0xff93c4), // 3
    COL(0xff8135), // 4
    COL(0xfff609), // 5
    COL(0x249ca3), // 6
    COL(0x78dc52), // 7
    COL(0x003fad), // 8
    COL(0x87f2ff), // 9
    COL(0x8e2ec4), // 10
    COL(0xa4839f), // 11
    COL(0x5c406c), // 12
    COL(0xe5cdc4), // 13
    COL(0x91463d), // 14
    COL(0x000000), // 15
};
````

So that means that the Palette mode is probably slower than the 16 bit mode but the framebuffer is half the size (as the 16 colors are hardcoded, could have been coded on a nibble so 1/4 the size...). I don't see any value to use it... Better to code a proper 256 palette mode in assembly.

### MicroPython classes

The fork of MicroPython for Meowbit provides:
 * The `SCREEN` class with only one method: 

````
def show(fb, mode)
- fb: framebuffer: bytearray(size) with size normally 160x128*2 (framebuf.RGB565) or 160x128 (framebuf.PL8) 
- mode: None (RGB565) or any integer (PL8)
````

The MicroPython `framebuf` class which is an helper on top of the `bytearray` whcih some high level primitives:

* `FrameBuffer.fill(color)`: Fill the entire screen with the specified color color (hexadecimal number such as white 0xffffff)
* `FrameBuffer.pixel(x, y , color)`: if the method does not give color, you can get the color value of the pixel at the specified position. If the color value is given, the specified pixel is set to the given color
* `FrameBuffer.hline(x, y, w, c)`: use a pixel with a thickness of 1 from the specified x/y coordinates with w as the pixel length and c for the color to draw a horizontal line
* `FrameBuffer.vline(x, y, h, c)`: use a pixel with a thickness of 1 from the specified x/y coordinates with h as the pixel length and c for the color to draw a vertical line
* `FrameBuffer.line(x1, x2, y1, y2, c)`: use the thickness of the pixel to be 1 from the specified x1/y1 coordinates, the x2/y2 coordinates to the end point, and c to draw a line segment for the color.
* `FrameBuffer.rect(x, y, w, h, c)`: draw a hollow rectangle with a width w, a height h, and a color c with the x/y coordinates as the top left corner of the rectangle.
* `FrameBuffer.fill_rect(x, y, w, h, c)`: draw a filled rectangle
* `FrameBuffer.text(s, x, y, c)`: s: string (this method can only display ASCII characters, which is the general English alphanumeric and common punctuation), x/y: the upper left corner of the character is the reference point coordinate 
c: write the character color to FrameBuffer
* `FrameBuffer.scroll(xstep, ystep)`: Moves the contents of the FrameBuffer according to the given vector, which will leave the footprint of the previous color in the FrameBuffer
* `FrameBuffer.blit (fbuf, x, y, key)`: blit to pos(x,y) except pixel of color key

And some custom methods (not working from SD, only from flash)

* `FrameBuffer.loadbmp("x")`: x: The name of the bmp format image stored in the drive letter, you need to have a .bmp suffix such as pic.bmp
* `FrameBuffer.loadgif('x', f)`: x: The name of the gif formatted image stored in the drive letter, with a .gif suffix such as pic.gif 






