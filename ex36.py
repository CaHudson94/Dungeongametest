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
help = ("Help", "help", "H", "h")
back = ("Back, back, B, b")
yes = ("yes", "y")
no = ("no", "n")
die = ("die", "Die", "I die", "I Die", "i die", "i Die", "dead", "Dead")
inventory = ("Inventory", "inventory", "I", "i")
quit = ("Quit", "quit", "Q", "q", "Exit", "exit", "E", "e")

dragon_in_room = False

game_state = {
    "inventory": []
    "start item": []
}

input_dict ={
    "keys": []
}

class Item(object):
    def __init__(self, name, description, take_me):
        self.name = name
        self.description = description
        self.take_me = take_me
        self.valid_choices = valid_choices

def pickup_converter(t_choice):
    for key in input_dict.keys():
        if t_choice in input_dict[key].valid_choices:

            if game_state.start_item:
                print "You have chosen your path! Only one may be taken, move along!"
                do_loop()

            elif key in input_dict.keys and key not in game_state.inventory:
                game_state.inventory.append(key)
                input_dict.keys.remove(key)
                print "You picked up %s, it has been added to your inventory" % input_dict[key].name
                print(item.take.me)
                do_loop()

            elif item in game_state.inventory:
                print ("You already have that.")
                do_loop()

            elif t_choice in back:
                print "Guess you don't want any of this junk, back to it."
                do_loop()

            else:
                print "You can't take that try something else, maybe try 'the item'."
                do_loop()

def do_loop():
    while True:
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
                elif closer in back:
                    print "Guess you don't need to look at anything, back to it."
                    do_loop()
                else:
                    print "That is not very helpful. Why don't you try something like yes or no?"

            elif lo_choice in item:
                print "You see %s, %s, and %s." % items
                closer = raw_input("Would you like to look closer?").lower()
                if closer in yes:
                    print closerlookitems
                elif closer in no:
                    print "Alright back to it then."
                    do_loop()
                elif closer in back:
                    print "Guess you don't need to look at anything, back to it."
                    do_loop()
                else:
                    print "That is not very helpful. Why don't you try something like yes or no?"

            elif lo_choice in back:
                print "Guess you don't need to look at anything, back to it."
                do_loop()

            else:
                print "That is not helpful! next time try looking at something in the room or just go back..."

        elif choice in take:
            t_choice = raw_input("What would you like to take?\n> ")
            pickup_converter()

        elif choice in lis:
            li_choice = raw_input("What would you like to listen to?\n> ")

        elif choice in ent:
            e_choice = raw_input("Where would you like to enter?\n> ").lower()
                if e_choice in door1:
                    return ldoor
                    do_loop()

                elif e_choice in door2:
                    return cdoor
                    do_loop()

                elif echoice in door3:
                    return rdoor
                    do_loop()

                else:
                    print "Try choosing a door next time?"
                    do_loop()

        elif choice in help:
            print "Things you can do: "
            print "Look, Take, Listen, Enter."
            print "These can be used with objects or doors!"
            print "Other commands include: "
            print "Yes, No, Back, Quit, and Die."
            do_loop()

        elif choice in die:
            if dragon_in_room:
                print "You decide to die here but there is a dragon, it toasts you alive then eats you in two bites"
            else:
                print "I don't know why but you chose to die, your neck snaps!"
                print "GAME OVER!"
                    restart = raw_input("Would you like to Restart?\n> ")
                    if restart in yes:
                        game_state["inventoy"] = []
                        entrance_hall()
                    elif restart in no:
                        exit(0)
                    else:
                        print "I will take that as a no."
                        exit(0)

        elif choice in quit:
            exit(0)

        else:
            print "That is not very helpful. Looking around or something or ask for help?"
            do_loop()

def dead(why):
    print why, "You have died!"
    print "GAME OVER!"
        restart = raw_input("Would you like to Restart?\n> ")
        if restart in yes:
            entrance_hall()
        elif restart in no:
            exit(0)
        else:
            print "I will take that as a no."
            exit(0)

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
    print "If you would like to see what you have use Inventory or I."
    print "Use back to make a different choice."

    doors = ("A Black door", "A Red door", "A Silver door")
    door1 = ("black door", "the black door", "a black door")
    door2 = ("red door", "the red door", "a red door")
    door3 = ("silver door", "the silver door", "a silver door")
    items = ("A Staff", "A Sword", "A Cloak")
    ldoor = troll_room()
    cdoor = lava_room()
    rdoor = goblin_room()

    staff = Item(
    name = "The Staff of Power"
    description = ("The Staff is tall and twisted, made of a deep dark wood and topped with an ever changing crystal.",
                    " It exudes power, pulsing and searing against the air.")
    take_me = "The torches blaze up, wind howles through the room, and lightning strikes the crystal atop it! You got The Staff of Power!"
    valid_choices = ("Staff", "staff", "A Staff", "a Staff", "A staff", "a staff", "The Staff",
    "the Staff", "The staff", "the staff")
    )
    input_dict.keys["staff"] = staff

    sword = Item(
    name = "The "
    description = "The Sword double edged and roughly three feet long but oddly light, it has intricit etchings on either side of the blades face. ",
    " Even with the fine detail their isn't a single blemish on it, you get the feeling you couldn't break it if you tried."
    take_me = ""
    valid_choices = ("Sword", "sword", "A Sword", "a Sword", "A sword", "a sword", "The Sword",
    "the Sword", "The sword", "the sword")
    )
    input_dict.keys.["sword"] = sword

    cloak = Item(
    name = "Nigh"
    description = "The Cloak is cool and warm, black and shimmering and all colors at once. At times you can't even really see it.",
    "It is a bit unnearving while also being calming, almost protective."
    take_me =
    valid_choices = ("Cloak", "cloak", "A Cloak", "a Cloak", "A cloak", "a cloak", "The Cloak",
    "the Cloak", "The cloak", "the cloak")
    )
    input_dict.keys.["cloak"] = cloak

    closerlookdoors = ("The Black door is so dark you have a hard time telling it is even there.",
                    "The Red door appears as if it is on fire and is even a little warm to the touch.",
                    "The Silver door is made of metal and is slightly cool to the touch.")

    closerlookitems = (staff.description, sword.description, cloak.description)

    roomlis = "Listening to the room you hear the torches crackling and a subtle thruming, as if the very air is vibrating."

    doorlis = (door1, door2, door3)

    door1 = ("Listening at the Black door you hear only the slightest, quietest breath of wind and an unsettling amount of nothing else.")

    door2 = ("Listening at the Red door you hear the crackle of fire, as if from more torches and a deep distant rumble.")

    door3 = ("Listening at the Silver door you hear running water, an odd snorting, and a very faint, very distant mixture of rumbling")

    do_loop()

def troll_room():


def goblin_room():


def lava_room():

def infinite_room():
    print "You find yourself in a black room."
    print "It is devoid of all color, life or light. It is not dark simply black."
    print "Even so you can see a door opposite you and the door that has just swung shut behind you."
    print "There is nothing here in fact the room is it self nothing."
    do_loop()

def dragon_chamber():
    dragon = True
    print

def treasure_room():
    print
