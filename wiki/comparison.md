## Boards comparison

I did a quick comparison of some cool boards currently sole (July 2019).
I personnaly don't own all of them, only the pygamer and the meowbit.

### Table

| Features | Pygamer | Pybadge LC | Pybadge | Meowbit | Brainpad arcade |
|:----------------------:|:-------------------------------------------:|:-------------------------------------------:|:-------------------------------------------:|:----------------------------------------------:|:-----------------------:|
| Manufacturer | Adafruit | Adafruit | Adafruit | Kittenbot | GHI |
| Price | $39.95 | $24.95 | $34.95 | $39.90 | $49.95 |
| MCU Manufacturer | Atmel | Atmel | Atmel | ST | ST |
| MCU Type | SAMD51 | SAMD51 | SAMD51 | STM32 | STM32 |
| MCU Ref | ATSAMD51J19 | ATSAMD51J19 | ATSAMD51J19 | STM32F401RET6 | STM32F401 |
| MCU Max Freq | 200 MHz | 200 MHz | 200 MHz | 84 MHz | 84 MHz |
| RAM | 192 KB | 192 KB | 192 KB | 96 KB | 96 KB |
| TFT | ST7075R | ST7075R | ST7075R | ST7735 | ST7735 ? |
| Screen Resolution | 1.8" 160x128, RGB565 with dimming backlight | 1.8" 160x128, RGB565 with dimming backlight | 1.8" 160x128, RGB565 with dimming backlight | 1.8" 160x128, RGB565 without dimming backlight | 1.8" 160x128 |
| Int Flash (bootloader) | 512 KB | 512 KB | 512 KB | 512 KB | 512 KB |
| Ext Flash | 8 MB (QSPI) | 2 MB (SPI) | 2 MB (SPI) | 2 MB (SPI) for MP and 4 MB (SPI) for U2F | ? |
| SD Cards | Micro SD | No | No | SD | No |
| Accelerometer / gyro | Triple Axis | No | Triple Axis | mp6050 | Yes |
| Light Sensor | Yes | Yes | Yes | Yes | ? |
| Temperature Sensor | No | No | No | Yes | ? |
| Audio output | DAC 12bits | DAC 12bits | DAC 12bits | PWM | PWM |
| Speaker | Connector | Buzzer | Buzzer | Buzzer | Buzzer |
| Headphone jack | Yes | Yes | Yes | No | No |
| JADAC | No | No | No | Yes | Yes |
| Battery | LiPo connector | LiPo connector | LiPo connector | LiPo connector | 3 AAA |
| Extensions | 2 FeatherWings strips1 JST1 I2C Grove | No | 2 FeatherWings strips1 JST1 I2C Grove | BBCMicro 40 pins goldfinger | D1-D7/PWR/3v3/GNDS1, S2 |
| Arduino | Yes (+ Arcada) | Yes (+ Arcada) | Yes (+ Arcada) | No | No |
| Makecode Arcade | Yes | Yes | Yes | Yes | Yes |
| Micropython | Not yet | Not yet | Not yet | Yes | No |
| CircuitPython | Yes | Yes | Yes | No | No |
| TinyCLR | No | No | No | No | Maybe |
| Dimensions | 101.6x60.0x19.5 (mm) | 85.7x54.6x 10.0 (mm) | 85.7x54.6x 10.0 (mm) | 52x76x12(mm) | ? |
| Debug | SWD | SWD | SWD | SWD | ? |
| My ranking | 1st | 4rd | 3rd | 2nd | 5th

### Personal Opinion

- From a pure technical point of view, I really like the pygamer, more than 2 times more performant (RAM and Clock) than the STM32F4
- Something nice for demoscene compos, the SAMD51 based boards have a 12bits audio DAC and the pygamer headphones and speaker connectors.
- Then.. from a developper point of view, the Meowbit is great, I prefer MicroPython over CircuitPython and the STM32F4 is easier to code than the ATSAMD51.
- Without removable storage (SD), I found the other baords less interesting. 
- Overall, the brainpad is quite limited and the most expensive so not a good deal.


### Some regrets

A few things I still don't get:

- Why the Meowbit TFT is connected thru SPI on the slow bus.... what could be more important than a fast display ?
- For the sake of simplicity and to save ports, all TFTs are connected thru SPI. Easy but hard to reach more than 30 FPS. A paralell , a LVDS or a MIPI-DSI interface would have been so cool...
- For the moment, pygamer is not supported my MicroPython, I'm working on it but... (CircuitPython is nice but quite slow)


