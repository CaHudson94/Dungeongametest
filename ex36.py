#This is my first game and it starts with a road map
#First room is entrance hall
#The final two rOoms are treasure and dragon

look = ("Look", "look")
take = ("Take", "take")
lis = ("Listen", "listen")
ent = ("Enter", "enter")
door = ("Door", "door", "the door", "The door","the Door", "The Door",
"Doors", "doors", "the doors", "The doors","the Doors", "The Doors",)
yes = ("yes", "y")
no = ("no", "n")

def do_loop():
    do_loop = True
    while do_loop:
        choice = raw_input("What do you choose to do?\n> ")
        if choice == look:
            lo_choice = raw_input("What would you like to look at?\n> ")

        elif choice == take
            t_choice = raw_input("What would you like to take?\n> ")

        elif choice == lis
            li_choice = raw_input("What would you like to listen to?\n> ")

        elif choice == ent
            e_choice = raw_input("Where would you like to enter?\n> ")

        else:
            print "That is not very helpful. Looking around or something?"

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

    r1doors = ("A Black door", "A Red door", "A Silver door")
    r1items = ("A Staff", "A Sword", "A Cloak")
    r1closerlook = ("The Black door is so dark you have a hard time telling it is even there.",
                    "The Red door appears as if it is on fire and is even a little warm to the touch.",
                    "The Silver door is made of metal and is slightly cool to the touch.")

    do_loop = True
    while do_loop:
        choice = raw_input("> ")
        if choice == look:
            lo_choice = raw_input("What would you like to look at?\n> ")
            if lo_choice == door:
                print "You see %s, %s, and %s." % room_one_doors
                closer = raw_input("Would you like to look closer?").lower()
                if closer == yes:
                    print "The Black door is so dark you have a hard time telling it is even there."
                    print "The Red door appears as if it is on fire and is even a little warm to the touch."
                    print "The Silver door is made of metal and is slightly cool to the touch."
                elif closer == no:
                    print "Alright back to it then."
                    look_loop = False
                else:
                    print "That is not very helpful. Why don't you try something like yes or no?"



def dragon_chamber():
    print

def treasure_room():
    print

    choice = raw_input("> ")
    if choice == look
        lo_choice = raw_input("What would you like to look at?")
        if lo_choice == door
            print "You see %s." %
            closer = raw_input("Would you like to look closer?").lower()
            if closer == yes

            else closer == no

    if choice == take
        t_choice = raw_input("What would you like to take?")

    if choice == lis
        li_choice = raw_input("What would you like to listen to?")

    if choice == ent
        e_choice = raw_input("Where would you like to enter?")
