## In progress!

This is a port of the Bad Apple animation on the Meowbit.

 - `badapple.py`: RGB565 version
 - `badapple_pal.py`: PAL16 Grayscale adaptive version
 
 In the PC folder, you'll find the python tools (not for Meowbit, to run with Python 3.7) to convert the images into one datafile.
 - `convert.py`
 
Original video decomposed in images is available here: https://github.com/ggnkua/Atari_ST_Sources/tree/master/ASM/Various/Cyril%20Lambin%20(fenarinarsa)/Bad%20Apple/original

Because I did not find a good python dithering library (and Pillow's Floyd Steinberg is not that great), I used the good old XnViewMP to convert (batch mode) the images in 160x128 and 16 colors. The result is pretty good

Then run `convert.py` to generate the datafile
