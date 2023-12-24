#!/usr/bin/env python3
import sys
from typing import Self


class SchematicPoint:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def get_neighboring_points(self) -> list[Self]:
        return [
            SchematicPoint(self.x - 1, self.y - 1),
            SchematicPoint(self.x, self.y - 1),
            SchematicPoint(self.x + 1, self.y - 1),
            SchematicPoint(self.x - 1, self.y),
            SchematicPoint(self.x + 1, self.y),
            SchematicPoint(self.x - 1, self.y + 1),
            SchematicPoint(self.x, self.y + 1),
            SchematicPoint(self.x + 1, self.y + 1),
        ]


class SchematicSymbol:
    point: SchematicPoint
    char: str

    def __init__(self, point, char):
        self.point = point
        self.char = char

    def __repr__(self):
        return f"Symbol: {self.char} at {self.point}"


class SchematicNumber:
    number: int
    points: list[SchematicPoint]

    def __init__(self, number, points):
        self.number = number
        self.points = points

    def __repr__(self):
        return f"Number: {self.number} spanning points {self.points}"

    def is_adjacent_to(self, symbol: SchematicSymbol):
        adjacencies = symbol.point.get_neighboring_points()
        for point in self.points:
            if point in adjacencies:
                return True
        return False


SM_IDLE = 0
SM_FINDING_NUMERIC = 1

DIGITS = "0123456789"


def parse() -> tuple[list[SchematicNumber], list[SchematicSymbol]]:
    x = 0
    y = 0

    numbers = []
    symbols = []

    current_number = 0
    current_number_points = []

    sm_state = SM_IDLE

    while byte := sys.stdin.read(1):
        point = SchematicPoint(x, y)

        if sm_state == SM_IDLE:
            if byte in DIGITS:
                sm_state = SM_FINDING_NUMERIC
                current_number = int(byte)
                current_number_points.append(point)

        elif sm_state == SM_FINDING_NUMERIC:
            if byte in DIGITS:
                current_number *= 10
                current_number += int(byte)
                current_number_points.append(point)
            else:
                numbers.append(SchematicNumber(current_number, current_number_points))
                current_number = 0
                current_number_points = []
                sm_state = SM_IDLE

        if byte not in DIGITS and byte not in ".\n":
            symbols.append(SchematicSymbol(point, byte))

        if byte == "\n":
            x = 0
            y += 1
        else:
            x += 1
    return numbers, symbols


numbers, symbols = parse()

gear_candidates = [symbol for symbol in symbols if symbol.char == "*"]

ratio_total = 0

for gear in gear_candidates:
    adjacent_numbers = []
    for number in numbers:
        if number.is_adjacent_to(gear):
            adjacent_numbers.append(number)
    if len(adjacent_numbers) == 2:
        ratio_total += adjacent_numbers[0].number * adjacent_numbers[1].number
print(ratio_total)
