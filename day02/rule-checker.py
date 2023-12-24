#!/usr/bin/env python3

RED_CUBE_COUNT = 12
GREEN_CUBE_COUNT = 13
BLUE_CUBE_COUNT = 14

import sys


def was_game_possible(draws):
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            if "blue" in color:
                count = int(color.removesuffix(" blue"))
                if count > BLUE_CUBE_COUNT:
                    return False
            elif "green" in color:
                count = int(color.removesuffix(" green"))
                if count > GREEN_CUBE_COUNT:
                    return False
            elif "red" in color:
                count = int(color.removesuffix(" red"))
                if count > RED_CUBE_COUNT:
                    return False
    # by exhaustion
    return True


total = 0

for line in sys.stdin:
    game_string, draws_string = line.split(":")
    game_id = int(game_string.removeprefix("Game "))
    draws = draws_string.strip().split(";")
    if was_game_possible(draws):
        total += game_id

print(total)
