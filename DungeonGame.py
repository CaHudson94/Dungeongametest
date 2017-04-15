#ex 36 and 43
#This is my first game and it starts with a road map
#First room is entrance hall
#The final two rooms are treasure and dragon
from sys import exit

game_state = {}


class Command(list):


    def __init__(self, name, valid_choices):
        self.name = name
        self.valid_choices = valid_choices

look = Command(
    name = 'Look',
    valid_choices = ('Look', 'look', 'L', 'l', 'Lo', 'lo'),
)
game_state['commands'].append['Look']

take = Command(
    name = 'Take',
    valid_choices = ('Take', 'take', 'T', 't'),
)
game_state['commands'].append['Take']

listen = Command(
    name = 'Listen',
    valid_choices = ('Listen', 'listen', 'Lis', 'lis',),
)
game_state['commands'].append['Listen']

enter = Command(
    name = 'Enter',
    valid_choices = ('Enter', 'enter', 'E', 'e'),
)
game_state['commands'].append['Enter']

help = Command(
    name = 'Help',
    valid_choices = ('Help', 'help', 'H', 'h'),
)
game_state['commands'].append['Help']

back = Command(
    name = 'Back',
    valid_choices = ('Back', 'back', 'B', 'b'),
)
game_state['commands'].append['Back']

yes = Command(
    name = 'Yes',
    valid_choices = ('yes', 'y'),
)
game_state['commands'].append['Yes']

no = Command(
    name = 'No',
    valid_choices = ('no', 'n'),
)
game_state['commands'].append['No']

die = Command(
    name = 'Die',
    valid_choices = ('die', 'Die', 'I die', 'I Die', 'i die',
    'i Die', 'dead', 'Dead'),
)
game_state['commands'].append['Die']

inventory = Command(
    name = 'Inventory',
    valid_choices = ('Inventory', 'inventory', 'I', 'i', 'inv', 'Inv'),
)
game_state['commands'].append['Inventory']

quit = Command(
    name = 'Quit',
    valid_choices = ('Quit', 'quit', 'Q', 'q'),
)
game_state['commands'].append['Quit']

interact = Command(
    name = 'Interact',
    valid_choices = ('Int', 'int', 'In', 'in'),
)
game_state['commands'].append['Interact']

door = ('Door', 'door', 'the door', 'The door','the Door', 'The Door',
'Doors', 'doors', 'the doors', 'The doors','the Doors', 'The Doors',)
item = ('Item', 'item', 'Items', 'items')
roomlisten = ('Room', 'room', 'The Room', 'the room', 'The room', 'the Room')


class Room(object):

    self.item = []
    self.enemie = []
    self.door = []


class Door(room):

    def __init__(self, name, listen, description, enter):
        self.name = name
        self.listen = listen
        self.description = description
        self.enter = enter


class Item(room):

    def __init__(self, name, description, take_me, valid_choices):
        self.name = name
        self.description = description
        self.take_me = take_me
        self.valid_choices = valid_choices


class Enemy(room):

    def __init__(self, name, description, listen, interact, slay_txt, die_txt, item, item_txt):
        self.name = name
        self.description = description
        self.listen = listen
        self.interact = interact
        self.slay_text = slay_txt
        self.die_text = die_txt
        self.item = item
        self.item_txt = item_txt

    def slay(self):
        global game_state
        print self.slay_text
        game_state['room']['items'][self.item]['name'] = self.item
        print self.item_txt

    def die(self):
        dead(self.die_txt)


def new_game():
    global game_state
    game_over = False
    game_state = {
        'player': {
            'inventory': [],
            'interaction': [], #not sure about this one
            },
        'room': {
            'listen': '',
            'items': {},
            'doors': {},
            'enemies': [],
            },
        'commands':[],
        'dead':[],
        }

    dragon = False

    unburnt = False

    entrance_hall()


def look_converter(look):
    if look in door:
        print game_state['room']['doors']['look']
        closer = raw_input('Would you like to look closer?').lower()
        if closer in yes:
            print game_state['room']['doors']['look']['closer']

        elif closer in no:
            print 'Alright back to it then.'

        elif closer in back:
            print 'Guess you don\'t need to look at anything, back to it.'

        else:
            print 'That is not very helpful. Why don\'t you try \
something like yes or no?'

    elif look in game_state['room'][item]['look']:
        print items['look']
        closer = raw_input('Would you like to look closer?').lower()
        if closer in yes:
            print items['look']['closer']

        elif closer in no:
            print 'Alright back to it then.'

        elif closer in back:
            print 'Guess you don\'t need to look at anything, back to it.'

        else:
            print 'That is not very helpful. Why don\'t you try \
something like yes or no?'


    elif look in back:
        print 'Guess you don\'t need to look at anything, back to it.'


    else:
        print 'That is not helpful! next time try looking at something \
in the room or just go back...'


def pickup_converter(pickup):
    for item in game_state.room.items():
        if pickup in game_state['room']['items'][item]['valid_choices']:

            if item in game_state.room.items and key not in game_state.inventory:
                game_state.inventory.append(item)
                game_state.room.items.remove(item)
                print (item.take_me)
                print 'You picked up %s, it has been added to your \
inventory' % game_state['room'][item]['name']

            elif item == 'Staff' or 'Sword' or 'Cloak' and item in game_state.inventory:
                print 'You have chosen your path! Only one may be taken, move along!'

            elif item in game_state.inventory:
                print ('You already have that.')

            elif pickup in back:
                print 'Guess you don\'t want any of this junk, back to it.'

            else:
                print 'You can\'t take that try something else, maybe try \'the item\'.''


def listen_converter(listen):
    for door in game_state['room']['doors']:
        if listen in game_state['room']['doors'][door]['valid_choices']:
            print game_state['room']['doors'][door]['listen']

        elif listen in roomlis:
            print game_state['room']['listen']

        elif listen in back:
            print 'Guess you don\'t want to hear anything then, back to it.'

        else:
            print 'You can\'t listen to that, silly.'


def entry_converter(enter):
    for door in game_state['room']['doors']:
        if enter in game_state['room']['doors'][door]['valid_choices']:
             return game_state['room']['doors'][door]['enter']

        elif enter in back:
            print 'Guess you don\'t want to go anywhere yet, back to it.'
            return None

        else:
            print ('Either that isn\'t a door, isn\'t in this room, or your just crazy!')
            return None


def ineract_converter(interact):
    for enemy in game_state['room']['enemies']
        if interact in game_state['room']['enemies'][enemy]['interact']['valid_choices']:
            return game_state['room']['enemies'][enemy]['slay']

        elif interact in listen:
            print game_state['room']['enemies'][enemy]['listen']

        elif interact in back:
            print 'Guess you don\'t want anything to do with this thing.'
            print 'Back to it then!'

        else:
            dead(game_state['room']['enemies'][enemy]['die'])


def command_prompt(yes_no):
    if yes_no in yes:
    commands = raw_input('What command would you like to see options for?\n> ')
        for command in game_state['commands']
            if commands in game_state['commands'][command]
                print game_state['commands'][command]['valid_choices']

    elif yes_no in no:
        print 'Guess you got what you need.'

    elif yes_no in back:
        print 'Guess you got what you need.'

    else:
        print 'That does not work here, try a yes or no next time.'


def quit(yes_no):
    if yes_no in yes:
        exit('Good Bye!')

    elif yes_no in no:
        print 'Alright back to the game then!'

    elif yes_no in back:
        print 'Alright back to the game then!'

    else:
        print 'It\'s a simple yes or no question...'
        print 'You know what, just die instead!'
        dead('Stupidity was your end')


def restart():
    restart = raw_input('Would you like to Restart?\n> ')
    if restart in yes:
        game_over = True
        new_game()
    elif restart in no:
        exit('Good Bye!')
    elif restart in back:
        print ('Guess you would like to keep going then.')
    else:
        print ('I will take that as a no.')
        exit('Good Bye!')


def action():
    while game_over == False:
        choice = raw_input('What action would you like to take?\n> ')

        if choice in look:
            look_converter(raw_input('What would you like to look at?\n> '))

        elif choice in take:
            pickup_converter(raw_input('What would you like to take?\n> '))

        elif choice in listen:
            listen_converter(raw_input('What would you like to listen to?\n> '))

        elif choice in enter:
            new_room = entry_converter(raw_input('Which door would you \
like to enter?\n> ').lower())
            if new_room:
                new_room()

        elif choice in interact:
            ineract_converter(raw_input('How would you like to interact \
with this creature?\n> '))

        elif choice in help:
            print 'Things you can do: '
            print game_state['commands']
            command_prompt(raw_input('Would you like to see the list of input options?\n> '))

        elif choice in inventory:
            print game_state['player']['inventory']

        elif choice in die:
            if dragon_in_room and unburnt:
                print 'You decide to die here but there is a dragon, \
it tries to toast you but fails so it decides to eat you instead!'
                print 'GAME OVER!'
                return restart()

            elif dragon_in_room:
                print 'You decide to die here but there is a dragon, \
it toasts you alive like a human shaped marshmallow!'
                print 'GAME OVER!'
                return restart()

            else:
                print 'I don\'t know why but you chose to die, your neck snaps!'
                print 'GAME OVER!'
                return restart()

        elif choice in quit:
            quit(raw_input('Are you sure you would like to quit?\n> ').lower())

        else:
            print 'That is not very helpful. Look around or something! Or ask for help?'

    print 'GAME OVER!'
    Victory = False
        if victory:
            print 'You have slain the dragon and escaped the dungeon!'
            print 'Congratulations on your successful journey!'
            print 'You claim your riches and retire to a grand castle!'
            play_again = raw_input('Would you like to play again?\n> ')
                if play_again in yes:
                    new_game()
                elif play_again in no:
                    exit('Good Game!')
                else:
                    print 'I will take that as a no.'
                    exit('Good Bye!')
        else:
            print game_state['dead'], 'You have died!'
            play_again = raw_input('Would you like to play again?\n> ')
                if play_again in yes:
                    new_game()
                elif play_again in no:
                    exit('Good Bye!')
                else:
                    print 'I will take that as a no.'
                    exit('Good Bye!')

class EntranceHall(room):

    def enter(self):
        print "\n\n\n"
        print "-" * 100
        print """
You wake up to find yourself in a large chamber lit by torches.
Looking around you see three doors and three items near them you can't make out.
Moving forward in the room a voice speaks to you from nowhere and everywhere.
'Welcome to The Trove!'
'Here you will find many things.'
'You will have only your wit, body, and the treasures of The Trove to depend on...'
'Make your choices wisely as your fate is in your own hands.'
'Will you find the path to freedom or fail as so many who came before...'
'Now go!'
\nFor now you may do a few things:
Use enter to go through doors.
Use listen to hear behind a door.
Use take to pick up items.
Use look to look at things(usually an item(s) or door(s)).
If you would like to see what you have use Inventory or I.
Use back to make a different choice.
"""
        doors = ("A Black door", "A Red door", "A Silver door")
        door1 = ("black door", "the black door", "a black door")
        door2 = ("red door", "the red door", "a red door")
        door3 = ("silver door", "the silver door", "a silver door")
        items = ("A Staff", "A Sword", "A Cloak")
        ldoor = troll_room()
        cdoor = lava_room()
        rdoor = goblin_room()

    staff = Item(
        name = 'The Staff of Power',
        description = """
The Staff is tall and twisted, \
made of a deep dark wood and topped with an ever changing crystal. \
It exudes power, pulsing and searing against the air.
""",
        take_me = """
The torches blaze up, wind howles through the room \
and lightning strikes the crystal atop it! \
You got The Staff of Power!
""",
        valid_choices = ('Staff', 'staff', 'A Staff', 'a Staff', 'A staff',
        'a staff', 'The Staff', 'the Staff', 'The staff', 'the staff'),
    )
    game_state['room']['items'].append['Staff']

    sword = Item(
        name = 'Sanguineus',
        description = """
The Sword is double edged and roughly three feet long, \
and oddly light for its size, it has intricit etchings on either side \
of the blades face. Even with the fine detail their isn't \
a single blemish on it, you get the feeling you couldn't break \
it if you tried.""",
        take_me = """
You lift the sword from the ground and the blade almost seems to hum \
in your hand. You marvel at how well balanced it is and how natural it fits \
your hand. It feels as though it were made just for you. You look down to \
find a sheath has appeared on you hip which you slide your new weapon into. \
It's a perfect fit, but why wouldn't it be.
""",
        valid_choices = ('Sword', 'sword', 'A Sword', 'a Sword', 'A sword',
        'a sword', 'The Sword', 'the Sword', 'The sword', 'the sword'),
    )
    game_state['room']['items'].append['Sword']

    cloak = Item(
        name = 'Nigh',
        description = """
The Cloak is cool and warm, black and shimmering like a moon lit pool, \
while also all colors at once. At times you can\'t even really see it. \
Looking at it is a bit unnerving while also calming, it almost feels protective. \
The cloth is untarnished, softer than a shadow, and carries the\
faintest smell of the first leaves of fall.
""",
        take_me = """
You pick up the cloak and wrap yourself in it. The cloth catches wind and \
rustles around you. As it settles it seems the sounds around you are clearer, \
while your breathing and movement seems hushed and almost not even there. \
You have to strain to hear your own breathing as if any sound coming from \
beneth the cloak is being hushed.
""",
        valid_choices = ('Cloak', 'cloak', 'A Cloak', 'a Cloak', "A cloak", "a cloak", "The Cloak", "the Cloak", "The cloak", "the cloak"),
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
