# WARNING: this is not official information, only in progress retro-engineering

## Hardware

The Meowbit has 4 storage capabilities:
 - [STM32F401](https://github.com/shazz/Meowbit-Experiments/raw/master/wiki/stm32f401re.pdf) built-in 512 KB flash, 
 - 2MB SPI flash (mounted by MicroPython) - Winbound [W25Q80BV](https://github.com/shazz/Meowbit-Experiments/raw/master/wiki/flash-W25Q80BV.pdf) connected to SPI2
 - 4MB SPI flash (mounted by the bootloader) - Winbound [W25X32](https://github.com/shazz/Meowbit-Experiments/raw/master/wiki/flash-W25X32.pdf) connected to SPI2
 - SD Card reader connected to SDIO interface

### STM32F40 built-in flash

 - 512 KB Flash, not exposed to the applications, reserved for the bootloader

code: https://github.com/KittenBot/uf2-meowbit/blob/fat/main_f4.c

````
#define BOARD_FLASH_SECTORS 8
#define BOARD_FLASH_SIZE (512 * 1024)
````

### 4MB SPI Flash

 - Winbound Winbound [W25X32](https://github.com/shazz/Meowbit-Experiments/raw/master/wiki/flash-W25X32.pdf) 4MB SPI flash, mounted by the bootloader to run U2F applications

````
// FLASH_BYTES = 0x80000
// PIN_FLASH_CS = PB_1
````

Setup by the bootloader:

[main_f4.c](https://github.com/KittenBot/uf2-meowbit/blob/fat/main_f4.c)
````C
static void initSpi(){
    // spi2 pin pb12~15
    rcc_periph_clock_enable(RCC_GPIOB);
    rcc_periph_clock_enable(RCC_SPI2);
    setup_output_pin(CFG_PIN_FLASH_CS);
    pin_set(CFG_PIN_FLASH_CS, 1);

    gpio_mode_setup(GPIOB, GPIO_MODE_AF, GPIO_PUPD_NONE, GPIO13 | GPIO14 | GPIO15);
    gpio_set_af(GPIOB, GPIO_AF5, GPIO13 | GPIO14 | GPIO15);

    spi_reset(SPI2);
    spi_init_master(SPI2, SPI_CR1_BAUDRATE_FPCLK_DIV_4, SPI_CR1_CPOL_CLK_TO_1_WHEN_IDLE,
                    SPI_CR1_CPHA_CLK_TRANSITION_2, SPI_CR1_DFF_8BIT, SPI_CR1_MSBFIRST);
    spi_enable_software_slave_management(SPI2);
    spi_set_nss_high(SPI2);
    spi_enable(SPI2);
    DMESG("SPI2 init");
}
````

[spiflash.c](https://github.com/KittenBot/uf2-meowbit/blob/fat/spiflash.c)
````C
	if (!hf2_mode) {
        if (flag == 2){
            usb_msc_init(usbd_dev, MSC_EP_IN, 64, MSC_EP_OUT, 64, USBMFGSTRING, "SPI Flash",
                         "42.00", 4096, read_block_flash, write_block_flash); // 2M flash, 512 byte per block
        } else {
            usb_msc_init(usbd_dev, MSC_EP_IN, 64, MSC_EP_OUT, 64, USBMFGSTRING, "UF2 Bootloader",
                         "42.00", UF2_NUM_BLOCKS, read_block, write_block);
        }
	}
	hf2_init(usbd_dev);

	winusb_setup(usbd_dev);
````

````
#define FLASH_PAGE_SIZE			256
#define FLASH_SECTOR_SIZE		4096
#define FLASH_SECTOR_COUNT		512
#define FLASH_BLOCK_SIZE		65536
#define FLASH_PAGES_PER_SECTOR	FLASH_SECTOR_SIZE/FLASH_PAGE_SIZE
#define W25X32_CHIPID				0xEF3016
````

### 2MB SPI Flash

 - Winbound [W25Q80BV](https://github.com/shazz/Meowbit-Experiments/raw/master/wiki/flash-W25Q80BV.pdf) 2MB SPI flash, mounted by MicroPython (in addition to SD cards) to run python applications

 - SPI1 42MHz max, SPI2 21MHz max
 - Using SPI-1: X5-X8, CS, CLK, MISO, MOSI, 3.3v, GND
 - Chip Select (CS) is connected to pin `PB1`

The flash is mounted by the MicroPython REPL at start. Mount Points are:

 - `/sd` (or `/sd`, `/sd2`, `/sd3`, `/sd4`). if `SKIPSD` file available on flash, will be skipped.
 - `/flash`

[mpconfigboard.h](https://github.com/shazz/micropython/blob/master/ports/stm32/boards/MEOWBIT/mpconfigboard.h)
````C
#define MICROPY_HW_ENABLE_STORAGE   (1)
#define MICROPY_HW_HAS_FLASH        (1)
#define MICROPY_HW_ENABLE_USB       (1)
#define MICROPY_HW_HAS_SDCARD       (1)
#define MICROPY_HW_ENABLE_INTERNAL_FLASH_STORAGE (0)
````

[main.c](https://github.com/shazz/micropython/blob/uf2/ports/stm32/main.c)
````C
    #if MICROPY_HW_ENABLE_USB
    pyb_usb_init0();
    #endif

    // Initialise the local flash filesystem.
    // Create it if needed, mount in on /flash, and set it as current dir.
    bool mounted_flash = false;
    #if MICROPY_HW_ENABLE_STORAGE
    mounted_flash = init_flash_fs(reset_mode);
    #endif

    bool mounted_sdcard = false;
    #if MICROPY_HW_HAS_SDCARD
    // if an SD card is present then mount it on /sd/
    if (sdcard_is_present()) {
        // if there is a file in the flash called "SKIPSD", then we don't mount the SD card
        if (!mounted_flash || f_stat(&fs_user_mount_flash.fatfs, "/SKIPSD", NULL) != FR_OK) {
            mounted_sdcard = init_sdcard_fs();
        }
    }
    #endif

    #if MICROPY_HW_ENABLE_USB
    // if the SD card isn't used as the USB MSC medium then use the internal flash
    if (pyb_usb_storage_medium == PYB_USB_STORAGE_MEDIUM_NONE) {
        pyb_usb_storage_medium = PYB_USB_STORAGE_MEDIUM_FLASH;
    }
    #endif

    // set sys.path based on mounted filesystems (/sd is first so it can override /flash)
    if (mounted_sdcard) {
        mp_obj_list_append(mp_sys_path, MP_OBJ_NEW_QSTR(MP_QSTR__slash_sd));
        mp_obj_list_append(mp_sys_path, MP_OBJ_NEW_QSTR(MP_QSTR__slash_sd_slash_lib));
    }
    if (mounted_flash) {
        mp_obj_list_append(mp_sys_path, MP_OBJ_NEW_QSTR(MP_QSTR__slash_flash));
        mp_obj_list_append(mp_sys_path, MP_OBJ_NEW_QSTR(MP_QSTR__slash_flash_slash_lib));
    }
````

## APIs

### Filesystem

The filesystem can be accessed using the VFS FAT APIs:
 - [VFS](https://github.com/shazz/micropython/blob/master/extmod/vfs.h): to mount, navigate in the VFS
 - [VFS FAT](https://github.com/shazz/micropython/blob/master/extmod/vfs_fat.h)
 - [FatFs](https://github.com/shazz/micropython/blob/master/lib/oofatfs/ff.h): Generic FAT FS Module

### Low Level 

#### 2MB SPI flash

Data can be read at the low level using the SPI API as in the [Example](https://github.com/shazz/micropython/blob/master/examples/meowbit/spiflash.py). This Example shows how to dialog with the SPI Flash:
 - `erase_chip()`
 - `erase()`
 - `read_block()`
 - `write_block()`
 - `getid()`
 - `wait()`

To init the communication with the flash using the SPI-2 bus (high speed), use the following code:
````python
# print("Initializing communication with the 2MB SPI flash")
cs = pyb.Pin('PB1')
cs.init(pyb.Pin.OUT_PP)
cs.high()
v = bytearray(4)
spi = SPI(2, SPI.MASTER, baudrate=42000000, polarity=0, phase=0)
wait()
getid()
````
### High Level

From a C module, to read/write file from any kind of storage, mount points should be retrieved.

Example code:

````C
#include "extmod/vfs.h"
#include "extmod/vfs_fat.h"

const char *p_out;
fs_user_mount_t *vfs_fat;
FRESULT res;
FIL fp;

// retrieve VFS FAT mount
mp_vfs_mount_t *vfs = mp_vfs_lookup_path(filename, &p_out);
if (vfs != MP_VFS_NONE && vfs != MP_VFS_ROOT) {
	vfs_fat = MP_OBJ_TO_PTR(vfs->obj);
}
else {
	printf("Cannot find user mount for %s\n", filename);
	return mp_const_none;
}    

res = f_open(&vfs_fat->fatfs, &fp, filename, FA_READ);
````

In MicroPython the os library provides all operations to navigate within the mounted storage:
````python
import os
os.listdir()
os.chdir('/')
os.listdir()
os.statvfs('/sd')
(32768, 32768, 1911819, 1903501, 1903501, 0, 0, 0, 0, 255)
os.statvfs('/flash')
(2048, 2048, 1014, 308, 308, 0, 0, 0, 0, 255)
````

statvfs structure:
 - `f_bsize` – file system block size
 - `f_frsize` – fragment size
 - `f_blocks` – size of fs in f_frsize units
 - `f_bfree` – number of free blocks
 - `f_bavail` – number of free blocks for unpriviliged users
 - `f_files` – number of inodes
 - `f_ffree` – number of free inodes
 - `f_favail` – number of free inodes for unpriviliged users
 - `f_flag` – mount flags
 - `f_namemax` – maximum filename length

## Bootloader

At boot, flash is mounted thru USB:
 - `Model`: Kittenbo UF2 Bootloader (42.0)
 - `Size`: 4.1MB
 - `SN`: 0065005A3237510833363831
 - `UUID`: 0042-0042
 - `Type`: FAT16

When running MicroPython, flash is mounted thru USB:
 - `Model`: uPy microSD Flash (1.00)
 - `Size`: 2.2MB
 - `SN`: 339B388B3237
 - `UUID`: DED6-76D5
 - `Type`: FAT12

## Performance

See CSV files:

 1. Frequencies impact

 - As the SD Cards use the `SDIO` interface (up to 48MHz), increasing CPU/Bus/DMA/Memory frequencies doesn't make a big difference. Less than 0.85% for bigger blocks.
 - 2MB flash is connected to `SPI2` so frequencies change have a big impact
 - `readinto()` is mostly 2 times faster than read()

Statistics for `readinto()`

 - SD Card:

|   fb  | block size | time in ms | bytes/ms | MB/s |      Bus      |   Interface  |   Type  |
|:-----:|:----------:|:----------:|:--------:|:----:|:-------------:|:------------:|:-------:|
|  4bpp |    10240   |   2.45233  |  4175.62 | 3.98 | APB2 (84 MHz) | SDIO (48MHz) | SD 64GB |
|  8bpp |    20480   |   5.75184  |  3560.60 | 3.40 | APB2 (84 MHz) | SDIO (48MHz) | SD 64GB |
| 16bpp |    40960   |   6.57845  |  6226.39 | 5.94 | APB2 (84 MHz) | SDIO (48MHz) | SD 64GB |

 - SPI 2MB Flash:

|   fb  | block size | time in ms | bytes/ms | MB/s |      Bus      |   Interface  |    Type   |
|:-----:|:----------:|:----------:|:--------:|:----:|:-------------:|:------------:|:---------:|
|  4bpp |    10240   |   4.1815   |  2448.88 | 2.34 | APB1 (42 MHz) | SPI2 (21MHz) | Flash 2MB |
|  8bpp |    20480   |   8.32055  |  2461.38 | 2.35 | APB1 (42 MHz) | SPI2 (21MHz) | Flash 2MB |
| 16bpp |    40960   |  16.61015  |  2465.96 | 2.35 | APB1 (42 MHz) | SPI2 (21MHz) | Flash 2MB |

 - SPI 2MB Flash

|   fb  | block size | time in ms | bytes/ms | MB/s |      Bus      |  Interface  |    Type   |
|:-----:|:----------:|:----------:|:--------:|:----:|:-------------:|:-----------:|:---------:|
|  4bpp |    10240   |   12.1663  |  841.67  | 0.80 | APB1 (14 MHz) | SPI2 (7MHz) | Flash 2MB |
|  8bpp |    20480   |   24.2449  |  844.71  | 0.81 | APB1 (14 MHz) | SPI2 (7MHz) | Flash 2MB |
| 16bpp |    40960   |   48.4243  |  845.86  | 0.81 | APB1 (14 MHz) | SPI2 (7MHz) | Flash 2MB |

## Source code

### W25Q80BV 2MB SPI flash:

 - [Meowbit spiflash.py](https://github.com/shazz/micropython/blob/master/examples/meowbit/spiflash.py)
 - [Adafruit W25Q80BV spiflash.py](https://github.com/SpotlightKid/micropython-stm-lib/blob/master/spiflash/spiflash.py)
 - [Adafruit W25Q80BV spiflash.py](https://github.com/manitou48/pyboard/blob/master/spiflash.py)

 