The following table shows the performance of my 3 software modes:
 - RGB656: same as the TFT framebuffer, no processing needed but 2 bytes per pixel so 40KB per frame.
 - PAL256: 8bpp, processing needed but 20KB per frame. Palettes fixed but selectable.
 - PAL16 : 4bpp, processing needed but 10KB per frame. Palettes fixed but selectable (C64, Apple2,..)

|  type  | average blitting time in ms |    CPU   |    AHB   |   APB1   |   APB2   |
|:------:|:---------------------------:|:--------:|:--------:|:--------:|:--------:|
| rgb565 |           93.6759           | 56000000 | 56000000 | 14000000 | 28000000 |
| rgb565 |           31.2421           | 84000000 | 84000000 | 42000000 | 84000000 |
| pal256 |           106.8659          | 56000000 | 56000000 | 14000000 | 28000000 |
| pal256 |            39.807           | 84000000 | 84000000 | 42000000 | 84000000 |
|  pal16 |           105.6661          | 56000000 | 56000000 | 14000000 | 28000000 |
|  pal16 |           39.0361           | 84000000 | 84000000 | 42000000 | 84000000 |

So as at 60 fps, 1 frame == 16.66ms, it seems it is not possible to reach more than 32 fps with the current mode.

Note that for some reasons, the TFT controller is attached to SPI2 which uses APB1 to communicate with the MCU RAM, limited to 42 MHz, even using the DMA:

Using:
````C
spi_transfer(screen->spi, bufinfo.len, p, NULL, 500);  // Uses the DMA
````
or
````C
HAL_SPI_Transmit(screen->spi->spi, p, bufinfo.len, 500); //No DMA used
````

Doesn't make any difference.