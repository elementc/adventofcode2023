import sys

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def scan_replace_digit_words(line):
    new_line = ""
    length = len(line)
    idx = 0
    while idx < length:
        if line[idx] in "123456789":
            new_line += line[idx]
        for original in replacements:
            if idx + len(original) < length:
                if line[idx : idx + len(original)] == original:
                    new_line += replacements[original]
        idx += 1
    return new_line


total = 0
for line in sys.stdin:
    fixed = scan_replace_digit_words(line)
    digits = [digit for digit in fixed if digit in "123456789"]
    value = int(digits[0] + "" + digits[-1])
    total += value
print(total)
