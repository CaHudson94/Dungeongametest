#ex 36 and 43
#This is my first game and it starts with a road map
#First room is entrance hall
#The final two rooms are treasure and dragon
from sys import exit

game_state = {}


class command(list):


    def __init__(self, name, valid_choices):
        self.name = name
        self.valid_choices = valid_choices

look = command(
    name = 'Look',
    valid_choices = ('Look', 'look', 'L', 'l', 'Lo', 'lo'),
)
game_state['commands'].append['Look']

take = command(
    name = 'Take',
    valid_choices = ('Take', 'take', 'T', 't'),
)
game_state['commands'].append['Take']

lis = command(
    name = 'Listen',
    valid_choices = ('Listen', 'listen', 'Lis', 'lis',),
)
game_state['commands'].append['Listen']

ent = command(
    name = 'Enter',
    valid_choices = ('Enter', 'enter', 'E', 'e'),
)
game_state['commands'].append['Enter']

help = command(
    name = 'Help',
    valid_choices = ('Help', 'help', 'H', 'h'),
)
game_state['commands'].append['Help']

back = command(
    name = 'Back',
    valid_choices = ('Back', 'back', 'B', 'b'),
)
game_state['commands'].append['Back']

yes = command(
    name = 'Yes',
    valid_choices = ('yes', 'y'),
)
game_state['commands'].append['Yes']

no = command(
    name = 'No',
    valid_choices = ('no', 'n'),
)
game_state['commands'].append['No']

die = command(
    name = 'Die',
    valid_choices = ('die', 'Die', 'I die', 'I Die', 'i die',
'i Die', 'dead', 'Dead'),
)
game_state['commands'].append['Die']

inventory = command(
    name = 'Inventory',
    valid_choices = ('Inventory', 'inventory', 'I', 'i', 'inv', 'Inv'),
)
game_state['commands'].append['Inventory']

quit = command(
    name = 'Quit',
    valid_choices = ('Quit', 'quit', 'Q', 'q'),
)
game_state['commands'].append['Quit']

interact = command(
    name = 'Interact',
    valid_choices = ('Int', 'int', 'In', 'in'),
)
game_state['commands'].append['Interact']

door = ('Door', 'door', 'the door', 'The door','the Door', 'The Door',
'Doors', 'doors', 'the doors', 'The doors','the Doors', 'The Doors',)
item = ('Item', 'item', 'Items', 'items')
roomlis = ('Room', 'room', 'The Room', 'the room', 'The room', 'the Room')

class room(object):

    self.items = []
    self.enemies = []
    self.doors = []


class door(room):

    def __init__(self, name, lis, description):
        self.name = name
        self.lis = lis
        self.description = description

class item(room):

    def __init__(self, name, description, take_me, valid_choices):
        self.name = name
        self.description = description
        self.take_me = take_me
        self.valid_choices = valid_choices

class enemies(room):

    def __init__(self, name, description, talk, attack, magic, sneak, die, slay):
        self.name = name
        self.description = description
        self.talk = talk
        self.attack = attack
        self.magic = magic
        self.sneak = sneak
        self.die = die
        self.sneak = sneak


def new_game():
    global game_state
    game_state = {
        'player': {
            'inventory': [],
            'attacks': [], #not sure about this one
            },
        'room': {
            'lis': '',
            'items': [],
            'doors': [],
            'enemies': [],
            },
        'commands':[]
        }

    dragon = False

    unburnt = False

    entrance_hall()


def listen_converter(li_choice):
    for door in game_state['room']['doors']:
        if li_choice in game_state['room']['doors'][door]['valid_choices']:
            return game_state['room']['doors'][door]['listen']

        elif li_choice in roomlis:
            return game_state['room']['lis']

        elif li_choice in back:
            print 'Guess you don\'t want to hear anything then, back to it.'
            return action()

        else:
            print 'You can\'t listen to that, silly.'
            return action()


def entry_converter(e_choice):
    for door in game_state['room']['doors']:
        if e_choice in game_state['room']['doors'][door]['valid_choices']:
             return game_state['room']['doors'][door]['enter']

        elif e_choice in back:
            print 'Guess you don\'t want to go anywhere yet, back to it.'
            return action()

        else:
            print ('Either that isn\'t a door, isn\'t in this room, or your just crazy!')
            return action()


def ineract_converter(int_choice):
    for enemy in game_state['room']['enemies']
        if int_choice in game_state['room']['enemies'][enemy]


def pickup_converter(t_choice):
    for item in game_state.room.items():
        if t_choice in game_state['room']['items'][item]['valid_choices']:

            if item in game_state.room.items and key not in game_state.inventory:
                game_state.inventory.append(item)
                game_state.room.items.remove(item)
                print (item.take_me)
                print "You picked up %s, \
it has been added to your inventory" % game_state['room'][item]['name']
                return action()

            elif item == "Staff" or "Sword" or "Cloak" and item in game_state.inventory:
                print "You have chosen your path! Only one may be taken, move along!"
                return action()

            elif item in game_state.inventory:
                print ("You already have that.")
                return action()

            elif t_choice in back:
                print "Guess you don\'t want any of this junk, back to it."
                return action()

            else:
                print "You can\'t take that try something else, maybe try \'the item\'."
                return action()


def restart():
    restart = raw_input("Would you like to Restart?\n> ")
    if restart in yes:
        new_game()
    elif restart in no:
        exit("Good Bye!")
    elif restart in back:
        print ("Guess you would like to keep going then.")
        return action()
    else:
        print "I will take that as a no."
        exit("Good Bye!")


def action():
    while True:
        choice = raw_input("What action would you like to take?\n> ")

        if choice in look:
            lo_choice = raw_input("What would you like to look at?\n> ")

            if lo_choice in door:
                print game_state['room']['doors']['look']
                closer = raw_input("Would you like to look closer?").lower()
                if closer in yes:
                    print game_state['room']['doors']['look']['closer']
                elif closer in no:
                    print "Alright back to it then."
                    return action()
                elif closer in back:
                    print "Guess you don't need to look",
                    print "at anything, back to it."
                    return action()
                else:
                    print "That is not very helpful. Why don't you try",
                    print " something like yes or no?"
                    return action()

            elif lo_choice in game_state['room'][item]['look']:
                print items['look']
                closer = raw_input("Would you like to look closer?").lower()
                if closer in yes:
                    print items['look']['closer']
                elif closer in no:
                    print "Alright back to it then."
                    return action()
                elif closer in back:
                    print "Guess you don't need to look",
                    print "at anything, back to it."
                    return action()
                else:
                    print "That is not very helpful. Why don't you try",
                    print " something like yes or no?"
                    return action()

            elif lo_choice in back:
                print "Guess you don't need to look at anything, back to it."
                return action()

            else:
                print "That is not helpful! next time try looking",
                print " at something in the room or just go back..."
                return action()

        elif choice in take:
            t_choice = raw_input("What would you like to take?\n> ")
            pickup_converter()

        elif choice in lis:
            li_choice = raw_input("What would you like to listen to?\n> ")
            listen_converter(li_choice)

        elif choice in ent:
            e_choice = raw_input("Which door would you",
                        " like to enter?\n> ").lower()
            entry_converter()

        elif choice in interact:
            int_choice = raw_input("How would you like to interact with this creature?\n> ")

        elif choice in help:
            print "Things you can do: "
            print game_state['commands']
            return action()

        elif choice in inventory:
            print game_state['player']['inventory']

        elif choice in die:
            if dragon_in_room and unburnt:
                print "You decide to die here but there is a dragon, \
it tries to toast you but fails so it decides to eat you instead!"
                print "GAME OVER!"
                return restart()
            elif dragon_in_room:
                print "You decide to die here but there is a dragon, \
it toasts you alive like a human shaped marshmallow!"
                print "GAME OVER!"
                return restart()
            else:
                print "I don't know why but you chose to die, your neck snaps!"
                print "GAME OVER!"
                return restart()

        elif choice in quit:
            check = raw_input("Are you sure you would like to quit?\n> ").lower()

            if check in yes:
                exit("Good Bye!")

            elif check in no:
                print "Alright back to the game then!"
                return action()

            elif check in back:
                print "Alright back to the game then!"
                return action()

            else:
                print "It's a simple yes or no question..."
                print "You know what just die instead!"
                dead("Stupidity was your end")

        else:
            print "That is not very helpful. Look around or something! Or ask for help?"
            return action()


def dead(why):
    print why, "You have died!"
    print "GAME OVER!"
    restart = raw_input("Would you like to Restart?\n> ")
    if restart in yes:
        new_game()
    elif restart in no:
        exit("Good Bye!")
    else:
        print "I will take that as a no."
        exit("Good Bye!")


def entrance_hall():
    print "\n\n\n"
    print "-" * 100
    print "You wake up to find yourself in a large chamber lit by torches."
    print "Looking around you see three doors and",
    print "three items near them you can't make out."
    print "Moving forward in the room a voice speaks",
    print "to you from nowhere and everywhere."
    print "'Welcome to The Trove!'"
    print "'Here you will find many things.'"
    print "'You will have only your wit, body, and the treasures of",
    print "The Trove to depend on...'"
    print "'Make your choices wisely as your fate is in your own hands.'"
    print "'Will you find the path to freedom or",
    print "fail as so many who came before...'"
    print "'Now go!'"
    print "\nFor now you may do a few things:"
    print "Use enter to go through doors."
    print "Use listen to hear behind a door."
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
        name = "The Staff of Power",
        description = ("The Staff is tall and twisted,",
        " made of a deep dark wood and topped with an ever changing crystal.",
        " It exudes power, pulsing and searing against the air."),
        take_me = '''The torches blaze up, wind howles through the room,\
        and lightning strikes the crystal atop it!\
        You got The Staff of Power!''',
        valid_choices = ("Staff", "staff", "A Staff", "a Staff", "A staff",
        "a staff", "The Staff", "the Staff", "The staff", "the staff"),
    )
    game_state['room']['items'].append['Staff']

    sword = Item(
        name = 'Sanguineus',
        description = '''The Sword double edged and roughly three feet long,\
        but oddly light, it has intricit etchings on either side\
        of the blades face. Even with the fine detail their isn't\
        a single blemish on it, you get the feeling you couldn't break\
        it if you tried.''',
        take_me = ' ',
        valid_choices = ("Sword", "sword", "A Sword", "a Sword", "A sword", "a sword", "The Sword", "the Sword", "The sword", "the sword"),
    )
    game_state['room']['items'].append['Sword']

    cloak = Item(
        name = "Nigh",
        description = "The Cloak is cool and warm, black and shimmering and all colors at once. At times you can't even really see it.", "It is a bit unnearving while also being calming, almost protective.",
        take_me = " ",
        valid_choices = ("Cloak", "cloak", "A Cloak", "a Cloak", "A cloak", "a cloak", "The Cloak", "the Cloak", "The cloak", "the cloak"),
    )
    game_state['room']['items'].append['Cloak']

    closerlookdoors = ("The Black door is so dark you have a hard time telling it is even there.",
                    "The Red door appears as if it is on fire and is even a little warm to the touch.",
                    "The Silver door is made of metal and is slightly cool to the touch.")

    closerlookitems = (staff.description, sword.description, cloak.description)

    roomlis = "Listening to the room you hear the torches crackling and a subtle thruming, as if the very air is vibrating."

    doorlis = (door1, door2, door3)

    door1 = ("Listening at the Black door you hear only the slightest, quietest breath of wind and an unsettling amount of nothing else.")

    door2 = ("Listening at the Red door you hear the crackle of fire, as if from more torches and a deep distant rumble.")

    door3 = ("Listening at the Silver door you hear running water, an odd snorting, and a very faint, very distant mixture of rumbling")

    return action()


def troll_room():
    
    pass


def goblin_room():

    pass


def lava_room():

    pass


def infinite_room():
    entries = 0
    if entries < 9 and entries > 0:
        print "Just as the room before..."
        door1 = ("Listening at the door you hear nothing, deafening, unending nothingness, Just as the door which lead you here. It was unsettling before and now it shakes you to your core.")

    print "You find yourself in a black room."
    print "It is devoid of all color, life or light. It is not dark simply black."
    print "Even so you can see a door opposite you and the door that has just swung shut behind you."
    print "There is nothing here in fact the room is it self nothing."
    return action()

    closerlookdoors = ("Just a simple plain brown wood door nothing descipt or unique about it or it's handle.")

    doorlis = (door1)

    door1 = ("Listening at the door you hear nothing, deafening, unending nothingness. Silence fails to describe the depth of nothingness you hear.")


def dragon_chamber():
    dragon = True
    print " "


def treasure_room():
    print " "


new_game()
