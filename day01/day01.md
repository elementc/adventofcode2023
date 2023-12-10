# part 1
I am having flashbacks to the bit in Wind Waker where the pirates load Link into the barrel to catapult him to the Forsaken Fortress. Let's hope it goes better for me than for him.

Okay, trust but verify, let's get these calibrations correct. Made `recover-calibrations.py`.
```
casey on WATERFALCON in adventofcode2023/day01 on  main [?] via 🐍 v3.11.6 
at 12:45:51 🍀 python recover-calibrations.py < input1
54331
```
# part 2
Oh, silly me, I need to also match written letters (I could write a thesis on requirements errors).

Same core logic applies but we also need to match like "one" in addition to "1".

```
casey on WATERFALCON in adventofcode2023/day01 on  main [?] via 🐍 v3.11.6 
at 12:45:53 🍀 cp recover-calibrations.py recover-calibrations-letters.py
```
I could probably come up with a stack of `sed`s but let's just do it in the new file.

## some time later

Okay i have a weird-bug, the UI says my number is wrong. I change the order of the `replacements` dict and... the value changes :O

The problem statement has a clue:
`eightwothree` -> 83
... ah, just seds wont do this, need to replace from the left and from the right, basically.

wrote `scan_replace_digit_words` and things work now:
```
casey on WATERFALCON in adventofcode2023/day01 on  main [?] via 🐍 v3.11.6 
at 13:44:53 🍀 python recover-calibrations-letters.py < input1
54518
```

_flight software is *go* for launch_