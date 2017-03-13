#This is my first game and it starts with a road map
#First room is entrance hall
#The final two rOoms are treasure and dragon
from sys import exit

look = ("Look", "look")
take = ("Take", "take")
lis = ("Listen", "listen")
ent = ("Enter", "enter")
door = ("Door", "door", "the door", "The door","the Door", "The Door",
"Doors", "doors", "the doors", "The doors","the Doors", "The Doors",)
item = ("Item, item, Items, items")
back = ("Back, back, B, b")
yes = ("yes", "y")
no = ("no", "n")
die = ("die", "Die", "I die", "I Die", "i die", "i Die", "dead", "Dead")
dragon_in_room = False

game_state = {
    inventory = None
}

def do_loop():
    while do_loop = True:
        choice = raw_input("What do you choose to do?\n> ")

        if choice in look:
            lo_choice = raw_input("What would you like to look at?\n> ")

            if lo_choice in door:
                print "You see %s, %s, and %s." % doors
                closer = raw_input("Would you like to look closer?").lower()
                if closer in yes:
                    print closerlookdoors
                elif closer in no:
                    print "Alright back to it then."
                    do_loop()
                else:
                    print "That is not very helpful. Why don't you try something like yes or no?"

            elif lo_choice in item
                print "You see %s, %s, and %s." % items
                closer = raw_input("Would you like to look closer?").lower()
                if closer in yes:
                    print closerlookitems
                elif closer in no:
                    print "Alright back to it then."
                    do_loop()
                else:
                    print "That is not very helpful. Why don't you try something like yes or no?"

            elif lo_choice in back
                print "Guess you don't need to look at anything, back to it."
                do_loop()

            else:
                print "That is not helpful! next time try looking at something in the room or just go back..."


        elif choice in take
            t_choice = raw_input("What would you like to take?\n> ")
                if t_choice = item1
                    print "You took %s, %s!" % item1, item1des
                    do_loop()
                    game_state.inventory(item1)
                elif t_choice = item2
                    print "You took %s, %s!" % item2, item2des
                    do_loop()
                    game_state.inventoy(item2)
                elif t_choice = item3
                    print "You took %s, %s!" % item3, item3des
                    do_loop()
                    game_state.inventoy(item3)
                elif t_choice in back
                    print "Guess you don't want any of this junk, back to it."
                    do_loop()
                else:
                    print "You can't take that try something else, maybe try 'the item'."
                    do_loop()


        elif choice == lis
            li_choice = raw_input("What would you like to listen to?\n> ")

        elif choice == ent
            e_choice = raw_input("Where would you like to enter?\n> ")

        elif choice == help
            print "Things you can do: "
            print "Look, Take, Listen, Enter."
            print "These can be used with objects as well such as doors!"

        elif choice == die
            if dragon_in_room:
                print "You decide to die here but there is a dragon, it toasts you alive then eats you in two bites"
            else:
                print "I don't know why but you chose to die, your neck snaps!"
                print "GAME OVER!"
                    restart = raw_input("Would you like to Restart?\n> ")
                    if restart == yes
                        entrance_hall()
                    elif restart == no
                        exit(0)
                    else:
                        print "I will take that as a no."
                        exit(0)

        else:
            print "That is not very helpful. Looking around or something or ask for help?"

def entrance_hall():
    print "You wake up to find yourself in a large chamber lit by torches."
    print "Looking around you see three doors and three items near them you can't make out."
    print "Moving forward in the room a voice speaks to you from nowhere and everywhere."
    print "'Welcome to The Trove!'"
    print "'Here you will find many things.'"
    print ""'You will have only your wit, body, and the treasures of The Trove to depend on...'
    print "'Make your choices wisely as your fate is in your own hands.'"
    print "'Will you find the path to freedom or fail as so many who came before...'"
    print "'Now go!'"
    print "\n For now you may do a few things:"
    print "Use enter to go through doors."
    print "Use listen to hear inside a room you haven't entered."
    print "Use take to pick up items."
    print "Use look to look at things(usually an item(s) or door(s))."



    doors = ("A Black door", "A Red door", "A Silver door")
    items = ("A Staff", "A Sword", "A Cloak")
    item1 = ("the staff")
    item1des = ("the torches blaze up, wind howles through the room, and lightning strikes the crystal atop it")
    item2 = ("the sword")
    item2des = ("")
    item3 = ("the cloak")
    item3des = ("")
    closerlookdoors = ("The Black door is so dark you have a hard time telling it is even there.",
                    "The Red door appears as if it is on fire and is even a little warm to the touch.",
                    "The Silver door is made of metal and is slightly cool to the touch.")
    closerlookitems = ("The Staff is tall and twisted, made of a deep dark wood and topped with an ever changing crystal.",
                    " It exudes power, pulsing and searing against the air.",
                    "\nThe Sword double edged and roughly three feet long but oddly light, it has intricit etchings on either side of the blades face. ",
                    " Even with the fine detail their isn't a single blemish on it, you get the feeling you couldn't break it if you tried.",
                    "\nThe Cloak is cool and warm, black and shimmering and all colors at once. At times you can't even really see it.",
                    "It is a bit unnearving while also being calming, almost protective.")
    roomlis = "Listening to the room you hear the torches crackling and a subtle thruming, as if the very air is vibrating."
    doorlis = (door1, door2, door3)
    door1 = ("Listening at the Black door you hear only the slightest, quietest breath of wind and an unsettling amount of nothing else.")
    door2 = ("Listening at the Red door you hear the crackle of fire, as if from more torches and a deep distant rumble.")
    door3 = ("Listening at the Silver door you hear running water, an odd snorting, and a very faint, very distant mixture of rumbling")


def dragon_chamber():
    dragon = True
    print

def treasure_room():
    print
