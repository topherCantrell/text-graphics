
board_art = """
..Y..Y..
..Y..Y..
YYYYYYYY
..Y..Y..
..Y..Y..
YYYYYYYY
..Y..Y..
..Y..Y..
"""

players_art = """
..GGGG.. | ...YY... | .RR...Y.
.G....G. | .YYYY... | R....Y.Y
.G....G. | .YYYY... | R....YYY
.....G.. | ...YY... | .RR..Y.Y
...GG... | ...YY... | ........
........ | ...YY... | .GGGGG..
...GG... | ..YYYY.. | ...G....
...GG... | .YYYYYY. | ...G....
"""

splash_art = """
GGG..... | GGG.RRR. | GGG.RRR.
.G...... | .G...R.. | .G...R..
.G...... | .G...R.. | .G...R..
.G...... | .G..RRR. | .G..RRR.
........ | ........ | ........
........ | ........ | ...YYY..
........ | ........ | ...Y....
........ | ........ | ...YYY..
------------------------------
YYY..... | YYY..GG. | YYY..GG.
.Y...... | .Y..G..G | .Y..G..G
.Y...... | .Y..GGGG | .Y..GGGG
.Y...... | .Y..G..G | .Y..G..G
........ | ........ | ........
........ | ........ | ...RRR..
........ | ........ | ...R....
........ | ........ | ...RRR..
------------------------------
.RRR.... | .RRR.YYY | .RRR.YYY
..R..... | ..R..Y.Y | ..R..Y.Y
..R..... | ..R..YYY | ..R..YYY
........ | ........ | ...GGGG.
........ | ........ | ...G....
........ | ........ | ...GGG..
........ | ........ | ...G....
........ | ........ | ...GGGG.
"""

wipers_art = """
YYYYYYYY | .Y****Y. | ..Y**Y.. | ...YY...
Y******Y | YYYYYYYY | ..Y**Y.. | ...YY...
Y******Y | *Y****Y* | YYYYYYYY | ...YY...
Y******Y | *Y****Y* | **Y**Y** | YYYYYYYY
Y******Y | *Y****Y* | **Y**Y** | YYYYYYYY
Y******Y | *Y****Y* | YYYYYYYY | ...YY...
Y******Y | YYYYYYYY | ..Y**Y.. | ...YY...
YYYYYYYY | .Y****Y. | ..Y**Y.. | ...YY...

Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y
Y******* | .Y****** | ..Y***** | ...Y**** | ....Y*** | .....Y** | ......Y* | .......Y

YYYYYYYY | ........ | ........ | ........ | ........ | ........ | ........ | ........
******** | YYYYYYYY | ........ | ........ | ........ | ........ | ........ | ........
******** | ******** | YYYYYYYY | ........ | ........ | ........ | ........ | ........
******** | ******** | ******** | YYYYYYYY | ........ | ........ | ........ | ........
******** | ******** | ******** | ******** | YYYYYYYY | ........ | ........ | ........
******** | ******** | ******** | ******** | ******** | YYYYYYYY | ........ | ........
******** | ******** | ******** | ******** | ******** | ******** | YYYYYYYY | ........
******** | ******** | ******** | ******** | ******** | ******** | ******** | YYYYYYYY


Y******* | ..Y***** | ....Y*** | ......Y* | ........ | ........ | ........ | ........
******** | .Y****** | ...Y**** | .....Y** | .......Y | ........ | ........ | ........
******** | Y******* | ..Y***** | ....Y*** | ......Y* | ........ | ........ | ........
******** | ******** | .Y****** | ...Y**** | .....Y** | .......Y | ........ | ........
******** | ******** | Y******* | ..Y***** | ....Y*** | ......Y* | ........ | ........
******** | ******** | ******** | .Y****** | ...Y**** | .....Y** | .......Y | ........
******** | ******** | ******** | Y******* | ..Y***** | ....Y*** | ......Y* | ........
******** | ******** | ******** | ******** | .Y****** | ...Y**** | .....Y** | .......Y
"""

cell_art = """
GG****** | ***GG*** | ******GG | ******** | ******** | ******** | ******** | ******** | ********
GG****** | ***GG*** | ******GG | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | GG****** | ***GG*** | ******GG | ******** | ******** | ********
******** | ******** | ******** | GG****** | ***GG*** | ******GG | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | GG****** | ***GG*** | ******GG
******** | ******** | ******** | ******** | ******** | ******** | GG****** | ***GG*** | ******GG

RR****** | ***RR*** | ******RR | ******** | ******** | ******** | ******** | ******** | ********
RR****** | ***RR*** | ******RR | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | RR****** | ***RR*** | ******RR | ******** | ******** | ********
******** | ******** | ******** | RR****** | ***RR*** | ******RR | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | ******** | ******** | ********
******** | ******** | ******** | ******** | ******** | ******** | RR****** | ***RR*** | ******RR
******** | ******** | ******** | ******** | ******** | ******** | RR****** | ***RR*** | ******RR
"""

wins_art = """
GGGGGGGG | ******** | ******** | GG****** | ***GG*** | ******GG | GG****** | ******GG
GGGGGGGG | ******** | ******** | GG****** | ***GG*** | ******GG | GG****** | ******GG
******** | ******** | ******** | GG****** | ***GG*** | ******GG | **G***** | *****G**
******** | GGGGGGGG | ******** | GG****** | ***GG*** | ******GG | ***GG*** | ***GG***
******** | GGGGGGGG | ******** | GG****** | ***GG*** | ******GG | ***GG*** | ***GG***
******** | ******** | ******** | GG****** | ***GG*** | ******GG | *****G** | **G*****
******** | ******** | GGGGGGGG | GG****** | ***GG*** | ******GG | ******GG | GG******
******** | ******** | GGGGGGGG | GG****** | ***GG*** | ******GG | ******GG | GG******

RRRRRRRR | ******** | ******** | RR****** | ***RR*** | ******RR | RR****** | ******RR
RRRRRRRR | ******** | ******** | RR****** | ***RR*** | ******RR | RR****** | ******RR
******** | ******** | ******** | RR****** | ***RR*** | ******RR | **R***** | *****R**
******** | RRRRRRRR | ******** | RR****** | ***RR*** | ******RR | ***RR*** | ***RR***
******** | RRRRRRRR | ******** | RR****** | ***RR*** | ******RR | ***RR*** | ***RR***
******** | ******** | ******** | RR****** | ***RR*** | ******RR | *****R** | **R*****
******** | ******** | RRRRRRRR | RR****** | ***RR*** | ******RR | ******RR | RR******
******** | ******** | RRRRRRRR | RR****** | ***RR*** | ******RR | ******RR | RR******
"""

mapping = {
    '.': 0,
    'R': 2,
    'G': 1,
    'Y': 3,
    '*': 0,
}

mask_map = {
    '.': 0,
    'R': 0,
    'G': 0,
    'Y': 0,
    '*': 3,
}

import led_8x8_bicolor

led_8x8_bicolor.print_images(board_art, mapping, 'board_art')
led_8x8_bicolor.print_images(players_art, mapping, 'players_art')
led_8x8_bicolor.print_images(splash_art, mapping, 'splash_art')
led_8x8_bicolor.print_images(wipers_art, mask_map, 'wipers_art')
led_8x8_bicolor.print_images(wipers_art, mapping, 'wipers_art')
led_8x8_bicolor.print_images(cell_art, mask_map, 'cell_art')
led_8x8_bicolor.print_images(cell_art, mapping, 'cell_art')
led_8x8_bicolor.print_images(wins_art, mask_map, 'wins_art')
led_8x8_bicolor.print_images(wins_art, mapping, 'wins_art')
