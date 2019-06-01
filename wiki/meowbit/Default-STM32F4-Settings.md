## Frequencies

From [system_stm32.c](https://github.com/micropython/micropython/blob/master/ports/stm32/system_stm32.c#L294):
````
const uint8_t AHBPrescTable[16] = {0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 6, 7, 8, 9};
const uint8_t APBPrescTable[8] = {0, 0, 0, 0, 1, 2, 3, 4};

RCC_OscInitStruct.PLL.PLLM = MICROPY_HW_CLK_PLLM;
RCC_OscInitStruct.PLL.PLLN = MICROPY_HW_CLK_PLLN;
RCC_OscInitStruct.PLL.PLLP = MICROPY_HW_CLK_PLLP;
RCC_OscInitStruct.PLL.PLLQ = MICROPY_HW_CLK_PLLQ;
#if defined(STM32F4)
RCC_ClkInitStruct.AHBCLKDivider  = RCC_SYSCLK_DIV1;
RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;
````

From [mpconfigboard.h](https://github.com/shazz/micropython/blob/master/ports/stm32/boards/MEOWBIT/mpconfigboard.h):
````
// HSE is 8MHz, CPU freq set to 84MHz
#define MICROPY_HW_CLK_PLLM (12)
#define MICROPY_HW_CLK_PLLN (336)
#define MICROPY_HW_CLK_PLLP (RCC_PLLP_DIV4)
#define MICROPY_HW_CLK_PLLQ (7)
#define MICROPY_HW_CLK_LAST_FREQ (1)
````

From [modmachine.c](https://github.com/micropython/micropython/blob/master/ports/stm32/modmachine.c#L312):
````
mp_int_t sysclk = mp_obj_get_int(args[0]);
mp_int_t ahb = sysclk;
mp_int_t apb1 = ahb / 4;
mp_int_t apb2 = ahb / 2;
````

From [powerctrl.c](https://github.com/micropython/micropython/blob/master/ports/stm32/powerctrl.c)
````
// Note: AHB freq required to be >= 14.2MHz for USB operation
RCC_ClkInitStruct.AHBCLKDivider = calc_ahb_div(sysclk / ahb);
RCC_ClkInitStruct.APB1CLKDivider = calc_apb_div(ahb / apb1);
RCC_ClkInitStruct.APB2CLKDivider = calc_apb_div(ahb / apb2);
````

That means:
````
PLLM : 12
PLLN : 336
PLLP : PLLP_DIV4
PLLQ : 7
AHBCLKDivider : RCC_SYSCLK_DIV1
APB1CLKDivider : RCC_HCLK_DIV4
APB2CLKDivider : RCC_HCLK_DIV2

VCO = HSE(PLL) * PLLN/PLLM = 8 * (336 / 12) = 224 (which is between the limits of 100 and 432)
USB = VCO / PLLQ = 224 / 7 = 32 (requires 48MHz)
PLL = VCO / PLLP = 224 / 4 = 56
CPU = VCO / PLLP = 224 / 4 = 56
SDIO = ? (requires <48MHz)
192 < PLNN < 432
PLLP can only be 2, 4, 6, or 8.
````

 - SYSCLK(CPU) = 56 
 - AHB = SYSCLK(CPU) = 56
 - APB1 = AHB / 4 = 14
 - APB2 = AHB / 2 = 28





