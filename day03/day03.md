# Part 1
Digging through schematics is a huge pain in the ass. I'm going to build the ultimate schematic parser so, no matter what goes wrong next, I won't have to do a ton of re-parsing.

So: I am making `uberparser.py`. We'll build lists of `numbers` and `symbols`, and notably will capture X-Y locations for both.
I will build a state machine to parse this character-by-character.

Business logic is reallly clean. Worked first try.

# Part 2
Oh, I figured there was some silliness remaining. Let's find those gears. I'll copy my parser into `gearsproggler.py` and give it a fixup.

Business logic was easy, worked first try. Time for a nice relaxing gondola ride.