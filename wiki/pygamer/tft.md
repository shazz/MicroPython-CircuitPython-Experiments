## TFT ST7735R Controller

[Datasheet](https://github.com/shazz/MicroPython-CircuitPython-Experiments/raw/master/wiki/pdfs/pygamer/ST7735R_V0.2.pdf)

### Differences with ST7735

The ST7735R is very similar to the ST7735 used by the Meowbit. The known differences are:
 - Power-up defaults are different, e.g. RGB or BGR mode.
 - RDID1 (0xDA) will return 0x5C on a 7735 but it is not specified on a 7735R.
 - Odd Power-Control register and possible the Gamma sequences.
 
Details: https://github.com/adafruit/Adafruit-ST7735-Library/blob/master/Adafruit_ST7735.cpp

### Pygamer integration

pins:

![Schematics](https://raw.githubusercontent.com/shazz/MicroPython-CircuitPython-Experiments/master/wiki/images/pygamer/MCU_pads.png))

````C
// TFT control pins
    { MP_OBJ_NEW_QSTR(MP_QSTR_TFT_LITE),  MP_ROM_PTR(&pin_PA01) }, //SERCOM1.1
    { MP_OBJ_NEW_QSTR(MP_QSTR_TFT_MOSI),  MP_ROM_PTR(&pin_PB15) }, //SERCOM4.3
    { MP_OBJ_NEW_QSTR(MP_QSTR_TFT_SCK),   MP_ROM_PTR(&pin_PB13) }, //SERCOM4.1
    { MP_OBJ_NEW_QSTR(MP_QSTR_TFT_RST),   MP_ROM_PTR(&pin_PA00) }, //SERCOM1.0
    { MP_ROM_QSTR(MP_QSTR_TFT_CS),        MP_ROM_PTR(&pin_PB12) }, //SERCOM4.0
    { MP_ROM_QSTR(MP_QSTR_TFT_DC),        MP_ROM_PTR(&pin_PB05) }, //I5/AIN7 ?
````

````C
typedef struct {
    mp_obj_base_t base;
    qstr name;
    uint8_t gpio_number;
    uint8_t gpio_function;
    uint32_t peripheral;
} mcu_pin_obj_t;

// void common_hal_busio_spi_construct(
//        busio_spi_obj_t *self,
//        const mcu_pin_obj_t * clock, 
//        const mcu_pin_obj_t * mosi,
//        const mcu_pin_obj_t * miso);

// void common_hal_displayio_fourwire_construct(
//        displayio_fourwire_obj_t* self,
//        busio_spi_obj_t* spi, 
//        const mcu_pin_obj_t* command,
//        const mcu_pin_obj_t* chip_select, 
//        const mcu_pin_obj_t* reset);  

void board_init(void) {
    busio_spi_obj_t* spi = &displays[0].fourwire_bus.inline_bus;
    
    // setup SPI using CLK=PB13=SERCOM4.1, MOSI=PB15SERCOM4.3 
    common_hal_busio_spi_construct(spi, &pin_PB13, &pin_PB15, NULL);
    common_hal_busio_spi_never_reset(spi);
    common_hal_busio_spi_configure(spi, 24000000, 0, 0, 8);

    // setup 4 wires SPI using Command=PB05, CS=PB12=SERCOM4.0, RS=PA00=SERCOM1.0
    displayio_fourwire_obj_t* bus = &displays[0].fourwire_bus;
    bus->base.type = &displayio_fourwire_type;
    common_hal_displayio_fourwire_construct(bus,
        spi,
        &pin_PB05,  // TFT_DC Command or data
        &pin_PB12,  // TFT_CS Chip select
        &pin_PA00); // TFT_RST Reset
        
    displayio_display_obj_t* display = &displays[0].display;
    display->base.type = &displayio_display_type;
    common_hal_displayio_display_construct(display,
        bus,
        160, // Width
        128, // Height
        0, // column start
        0, // row start
        270, // rotation
        16, // Color depth
        MIPI_COMMAND_SET_COLUMN_ADDRESS, // Set column command
        MIPI_COMMAND_SET_PAGE_ADDRESS, // Set row command
        MIPI_COMMAND_WRITE_MEMORY_START, // Write memory command
        0x37, // set vertical scroll command
        display_init_sequence,
        sizeof(display_init_sequence),
        &pin_PA01,  // backlight pin
        1.0f, // brightness (ignored)
        true, // auto_brightness
        false, // single_byte_bounds
        false); // data_as_commands
}
````
