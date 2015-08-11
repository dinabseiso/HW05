#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys

# Body

def introduction(username):
    username = sys.argv[1]
    print( "Hello " + username)
    return username

def infinite_stairway_room(username, count=0):
    print username + " walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light.'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print username + ' takes the stairs'
        if (count > 0):
            print "but " + username + " is not happy about it"
        infinite_stairway_room(username, count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(username):
    print "This room is full of gold.  How much does " + username + " take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, " + username + " is not greedy, " + username + " wins!"
    else:
        print(username + " is a greedy bastard, but a new door materializes!")
        infinite_stairway_room(username)


def bear_room(username):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is " + username + " going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        if next == ("take honey" or "honey" or "take"):
            dead("The bear looks at " + username + " then slaps their face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. " + username + " can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews " + username + "'s leg off.")
        elif next == "open door" or "open" or "door" and bear_moved:
            gold_room(username)
        else:
            print "I got no idea what that means."


def cthulhu_room(username):
    print "Here " + username + " sees the great evil Cthulhu."
    print "He, it, whatever stares at " + username + " and " + username + " goes insane."
    print "Does " + username + " flee for " + username + "'s life or does Cthulhu eat " + username + "'s head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    username = sys.argv[1]
    print( "Hello " + username)
    print username + " is in a dark room."
    print "There is a door to " + username + "'s right and left."
    print "Which one does " + username + " take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    else:
        dead( username + " stumbles around the room until " + username + "starves.")

if __name__ == '__main__':
    main()
