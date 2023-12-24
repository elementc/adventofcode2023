#!/usr/bin/env python3

import sys


def get_game_power(draws):
    red_min = 0
    green_min = 0
    blue_min = 0

    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            if "blue" in color:
                count = int(color.removesuffix(" blue"))
                if count > blue_min:
                    blue_min = count
            elif "green" in color:
                count = int(color.removesuffix(" green"))
                if count > green_min:
                    green_min = count
            elif "red" in color:
                count = int(color.removesuffix(" red"))
                if count > red_min:
                    red_min = count

    return red_min * green_min * blue_min


total = 0

for line in sys.stdin:
    game_string, draws_string = line.split(":")
    draws = draws_string.strip().split(";")
    total += get_game_power(draws)

print(total)
