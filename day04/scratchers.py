#!/usr/bin/env python3
import sys


def get_numbers_from_string(string) -> list[int]:
    numerics = string.split(" ")
    return [int(numeric) for numeric in numerics if numeric != ""]


card_winnings = []

for line in sys.stdin:
    cardID, cardContents = line.split(":")
    luckyNumbersString, myNumbersString = cardContents.split("|")
    luckyNumbers = get_numbers_from_string(luckyNumbersString)
    myNumbers = get_numbers_from_string(myNumbersString)
    match_count = len([_ for _ in myNumbers if _ in luckyNumbers])
    card_winnings.append(match_count)

card_counter = [1 for _ in range(len(card_winnings))]

for i in range(len(card_winnings)):
    this_card_winnings = card_winnings[i]
    if this_card_winnings > 0:
        for x in range(1, this_card_winnings + 1):
            card_counter[i + x] += card_counter[i]

print(sum(card_counter))
