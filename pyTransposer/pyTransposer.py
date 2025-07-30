# python -m pip install pytransposer
# python -m pip install colorama

import os
import sys
import random
from colorama import Fore, Style, init
import pytransposer.transposer as tr

sys.path.append('../lib')
from stringUtils import fitl


def get_random_colorama_fore():
        """Returns a random foreground color constant from colorama.Fore."""
        colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        return random.choice(colors)


def transpose_chord_range(chord, targetKey, intervalRange) -> None:

    random_fore_color = get_random_colorama_fore()

    for interval in range(intervalRange):
        result = tr.transpose_chord(chord, interval, targetKey)
        print(f"{random_fore_color}{fitl(chord, 5)} {fitl(interval, 8)} {fitl(targetKey, 4)} ->  {fitl(result, 7)}{Style.RESET_ALL}")


def transpose_chord(chord, targetKey, interval) -> None:

    random_fore_color = get_random_colorama_fore()
    result = tr.transpose_chord(chord, interval, targetKey)
    print(f"{random_fore_color}{fitl(chord, 5)} {fitl(interval, 8)} {fitl(targetKey, 4)} ->  {fitl(result, 7)}{Style.RESET_ALL}")


if __name__ == '__main__':

    os.system('cls')
    
    print(f'{fitl("Chord", 5)} {fitl("Interval", 8)} {fitl("Key", 4)}     {fitl("Result", 7)}')
    # transpose_chord_range('C', 'C', 1)
    # transpose_chord_range('C', 'C#', 1)
    # transpose_chord_range('C', 'D', 1)
    # transpose_chord_range('C', 'C', 13)
    # transpose_chord_range('C#', 'C', 13)
    # transpose_chord_range('Db', 'C', 13
    # transpose_chord_range('D', 'C', 13)
    # transpose_chord_range('B#', 'C', 13)
    transpose_chord('C', 'Eb', 3)
    transpose_chord('C', 'D#', 3)
    transpose_chord('F', 'C', 7)
    transpose_chord('F', 'C', 8)
    transpose_chord('F', 'Eb', 8)
    print()

