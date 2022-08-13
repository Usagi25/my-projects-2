# Display my pool table balls
# Andrew Zalesak August 3rd, 2022

"""
Example output

...

#############
#     Y     #
#    y G    #
#   O 8 g   #
#  R o b S  #
# r p P B s #
#############

Condition met: Y in first position.
Condition met: 8 in fifth position.

Swaps used: 5
Rotations used: 1

...

This ASCII display is 13 characters across
    and 7 characters tall.

I can store the arrangement as a simple list.

Commands:

-swap -G -p ... swap G and p
-rotate -ccw ... rotate counter-clockwise
-help ... help
-reset ... resets board to original position
-new ... resets boards to new random position

"""

"""
Things to do:
Add function that rotates position
Add function that checks if position is winning.
    Such a function needs to check whether pos[5] == "8" and pos[0] == "Y".
    Then, for each of balls[i] for [0:7], find index of it and balls[i+8] and
    see if they are adjacent. 0 with 1 and 2; 1 with 0, 2, 3, and (4); 2 with 0,
    1, (4), and 5; 3 with 1, (4), 6, and 7; 5 with 2, (4), 8, and 9; 6 with 3,
    7, 10, and 11; 7 with 3, (4), 6, 8, 11, and 12; 8 with (4), 5, 7, 9, 12, and
    13; 9 with 5, 8, 13, and 14; 10 with 6 and 11; 11 with 6, 7, 10, and 12; 12
    with 7, 8, 11, and 13; 13 with 8, 9, 12, and 14; 14 with 9 and 13.
"""

import random

game_over = False

pos = {}

balls_solids = ["Y", "S", "B", "P", "O", "G", "R"]
balls_stripes = [x.lower() for x in balls_solids]
balls_eight = ["8"]
balls = balls_solids + balls_eight + balls_stripes

pairing = {0: {1, 2},
           1: {0, 2, 3},
           2: {0, 1, 4, 5},
           3: {1, 4, 6, 7},
           4: {1, 2, 3, 5, 7, 8},
           5: {2, 4, 8, 9},
           6: {3, 7, 10, 11},
           7: {3, 4, 6, 8, 11, 12},
           8: {4, 5, 7, 9, 12, 13},
           9: {5, 8, 13, 14},
           10: {6, 11},
           11: {6, 7, 10, 12},
           12: {7, 8, 11, 13},
           13: {8, 9, 12, 14},
           14: {9, 13}}

# List takes O(n) search time but set takes O(1)
# set([a,b,c]) OR {a, b, c}

def check_pairs():
    if pos["Y"] != 0:
        return False
    if pos["8"] != 4:
        return False
    for solid, striped in zip(balls_solids, balls_stripes):
        if pos[solid] not in pairing[pos[striped]]:
            return False
    return True


def new_position():
    draw = random.sample(balls, 15)
    for i, ball in enumerate(draw):
        pos[ball] = i

    
def swap(first, second):
    newpos = pos
    """
    first_index = newpos.index(first)
    second_index = newpos.index(second)
    newpos[first_index] = second
    newpos[second_index] = first
    """
    temp = newpos[first]
    newpos[first] = newpos[second]
    newpos[second] = temp
    return(newpos)


def display():
    # This needs to be fixed. pos[0] doesn't work.
    posflip = {v: k for k, v in pos.items()}
    print("#" * 13)
    print("#    ", posflip[0], "    #")
    print("#   ", " ".join([posflip[1], posflip[2]]), "   #")
    print("#  ", " ".join([posflip[3],posflip[4], posflip[5]]), "  #")
    print("# ", " ".join([posflip[6], posflip[7], posflip[8], posflip[9]]), " #")
    print("#", " ".join([posflip[10], posflip[11], posflip[12], posflip[13], posflip[14]]), "#")
    print("#" * 13)
    print("\n" + "Swaps used: " + str(num_swaps))
    if check_pairs():
        print("You have won!")


#pos = new_position()
new_position()
num_swaps = 0
while not game_over:
    display()
    while True:
        action = input("Enter a pair of balls to swap: ")
        if len(action) == 2:
            if action[0] != action[1]:
                if (action[0] in balls) and (action[1] in balls):
                    num_swaps += 1
                    break
    pos = swap(action[0], action[1])
