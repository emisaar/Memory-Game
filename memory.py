"""
Game: Memory (May 11th, 2022)
Student 1: Alejandro Díaz Villagómez | A01276769
Student 2: Emiliano Saucedo Arriola | A01659258

Exercises:

1. Count and print how many taps occur.
2. Detect when all tiles are revealed.
3. Center single-digit tile. [DONE by Emiliano]
4. Use words instead of tiles. [DONE by Emiliano]
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0
turned_cards = 0

word_tiles = {0: 'apple', 1: 'bee', 2: 'corn', 3: 'doll', 4: 'elf', 5: 'fork', 6: 'git', 7: 'horse', 8: 'ignite', 9: 'jewel',
              10: 'key', 11: 'lime', 12: 'mom', 13: 'nurse', 14: 'onion', 15: 'pear', 16: 'queen', 17: 'root', 18: 'snake', 19: 'toy',
              20: 'uncle', 21: 'vowel', 22: 'wax', 23: 'xmas', 24: 'yield', 25: 'zap', 26: 'army', 27: 'bun', 28: 'can', 29: 'dog',
              30: 'eel', 31: 'forest', 32: 'apple', 33: 'bee', 34: 'corn', 35: 'doll', 36: 'elf', 37: 'fork', 38: 'git', 39: 'horse',
              40: 'ignite', 41: 'jewel', 42: 'key', 43: 'lime', 44: 'mom', 45: 'nurse', 46: 'onion', 47: 'pear', 48: 'queen', 49: 'root',
              50: 'snake', 51: 'toy', 52: 'uncle', 53: 'vowel', 54: 'wax', 55: 'xmas', 56: 'yield', 57: 'zap', 58: 'army', 59: 'bun', 60: 'can',
              61: 'dog', 62: 'eel', 63: 'forest'}


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    # Counting taps
    global taps
    taps += 1

    """Switch lines according to game mode (numbers or words)"""
    # if mark is None or mark == spot or tiles[mark] != tiles[spot]:
    if mark is None or mark == spot or word_tiles[mark] != word_tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Counting revealed cards (pairs)
        global turned_cards
        turned_cards += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        """Switch lines according to game mode (numbers or words)"""
        # goto(x + 25, y + 2) # To center numbers
        goto(x + 25, y + 15)  # To center words

        color('black')

        """Switch lines according to game mode (numbers or words)"""
        # write(tiles[mark], align = 'center', font = ('Arial', 30, 'normal')) # For numbers
        write(word_tiles[mark], align='center', font=(
            'Consolas', 11, 'normal'))  # For tiles

    goto(0, 210)

    """Showing taps in game"""
    write(taps, font=("Courier", 15, "bold"))
    update()

    """All cards are revealed"""
    if turned_cards == 32:
        up()
        goto(0, 0)
        color('white')
        write("YOU WIN!",  align="center", font=("Courier", 30, "italic"))
    ontimer(draw, 100)


"""Switch lines according to game mode (numbers or words)"""
# shuffle(tiles)
shuffle(word_tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
