import sys

total = 0
for line in sys.stdin:
    digits = [digit for digit in line if digit in "0123456789"]
    total += int(digits[0] + digits[-1])
print(total)
