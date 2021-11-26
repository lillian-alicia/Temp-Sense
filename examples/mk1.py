import st7789
import PIL, sys

disp = ST7789.ST7789(
        height = 240,
        rotation = 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left=0 
        offset_top = 0
    )

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

