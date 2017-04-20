#ex 36 and 43
#This is my first game and it starts with a road map
#First room is entrance hall
#The final two rooms are treasure and dragon
from sys import exit

game_state = {}
dragon = None
unburnt = None
victory = None
game_over = None
no_enemy = None

door = ('Door', 'door', 'the door', 'The door','the Door', 'The Door',
'Doors', 'doors', 'the doors', 'The doors','the Doors', 'The Doors',)
item = ('Item', 'item', 'Items', 'items')
roomlisten = ('Room', 'room', 'The Room', 'the room', 'The room', 'the Room')

class Command(object):

    def __init__(self, name, valid_choices):
        self.name = name
        self.valid_choices = valid_choices


class Door(object):

    def __init__(self, name, listen, glance, description, enter, valid_choices):
        self.name = name
        self.listen = listen
        self.glance = glance
        self.description = description
        self.enter = enter
        self.valid_choices = valid_choices


class Item(object):

    def __init__(self, name, item_look, description, take_me, valid_choices):
        self.name = name
        self.item_look = item_look
        self.description = description
        self.take_me = take_me
        self.valid_choices = valid_choices


class Enemy(object):

    global game_over
    global game_state

    def __init__(self, name, description, listen, Sword, Staff, Cloak,
    slay_txt, die_txt, item, item_txt, valid_choices, weapon):
        self.name = name
        self.description = description
        self.listen = listen
        self.Sword = Sword
        self.Staff = Staff
        self.Cloak = Cloak
        self.slay_text = slay_txt
        self.die_text = die_txt
        self.item = item
        self.item_txt = item_txt
        self.valid_choices = valid_choices
        self.weapon = weapon

    def write(self):
        game_state['room']['enemies']['name'] = [self.name]
        game_state['room']['enemies']['description'] = [self.description]
        game_state['room']['enemies']['listen'] = [self.listen]
        game_state['room']['enemies']['valid_choices'] = [self.valid_choices]
        game_state['player']['interactions']['Sword'] = [self.Sword]
        game_state['player']['interactions']['Staff'] = [self.Staff]
        game_state['player']['interactions']['Cloak'] = [self.Cloak]
        game_state['dead'] = [self.die_text]

    @classmethod
    def kill_or_die(self):

        if self.weapon == 'sword':
            if self.Sword == 'slay':
                print self.slay_text
                game_state['room']['items'][self.item]['name'] = self.item
                print self.item_txt
            elif self.Sword == 'die':
                game_over = True
        elif self.weapon == 'staff':
            if self.Staff == 'slay':
                print self.slay_text
                game_state['room']['items'][self.item]['name'] = self.item
                print self.item_txt
            elif self.Staff == 'die':
                game_over = True
        elif self.weapon == 'cloak':
            if self.Cloak == 'slay':
                print self.slay_text
                game_state['room']['items'][self.item]['name'] = self.item
                print self.item_txt
            elif self.Cloak == 'die':
                game_over = True

def new_game():
    global game_state
    global dragon
    global unburnt
    global victory
    global game_over
    global no_enemy
    game_state = {
        'player': {
            'inventory': {},
            'interactions': {
                'Sword': [],
                'Staff': [],
                'Cloak': [],
                },
            },
        'room': {
            'listen': [],
            'items': {},
            'doors': {},
            'enemies': {
                'name': [],
                'description': [],
                'listen': [],
                'valid_choices': [],
                },
            },
        'starting_items': [],
        'commands': {},
        'dead': [],
        }

    dragon = False

    unburnt = False

    victory = False

    game_over = False

    no_enemy = True

    game_state['commands']['Look'] = Command(
        name = 'Look',
        valid_choices = ('Look', 'look', 'L', 'l', 'Lo', 'lo'),
    )

    game_state['commands']['Take'] = Command(
        name = 'Take',
        valid_choices = ('Take', 'take', 'T', 't'),
    )

    game_state['commands']['Listen'] = Command(
        name = 'Listen',
        valid_choices = ('Listen', 'listen', 'Lis', 'lis',),
    )

    game_state['commands']['Enter'] = Command(
        name = 'Enter',
        valid_choices = ('Enter', 'enter', 'E', 'e'),
    )

    game_state['commands']['Help'] = Command(
        name = 'Help',
        valid_choices = ('Help', 'help', 'H', 'h'),
    )

    game_state['commands']['Back'] = Command(
        name = 'Back',
        valid_choices = ('Back', 'back', 'B', 'b'),
    )

    game_state['commands']['Yes'] = Command(
        name = 'Yes',
        valid_choices = ('yes', 'y'),
    )

    game_state['commands']['No'] = Command(
        name = 'No',
        valid_choices = ('no', 'n'),
    )

    game_state['commands']['Die'] = Command(
        name = 'Die',
        valid_choices = ('die', 'Die', 'I die', 'I Die', 'i die',
        'i Die', 'dead', 'Dead'),
    )

    game_state['commands']['Inventory'] = Command(
        name = 'Inventory',
        valid_choices = ('Inventory', 'inventory', 'I', 'i', 'inv', 'Inv'),
    )

    game_state['commands']['Quit'] = Command(
        name = 'Quit',
        valid_choices = ('Quit', 'quit', 'Q', 'q'),
    )

    game_state['commands']['Interact'] = Command(
        name = 'Interact',
        valid_choices = ('Int', 'int', 'In', 'in', 'Interact', 'interact'),
    )

    game_state['commands']['Use Sword'] = Command(
        name = 'Use Sword',
        valid_choices = ('Use Sword', 'use sword', 'Use sword', 'use Sword'),
    )

    game_state['commands']['Use Staff'] = Command(
        name = 'Use Staff',
        valid_choices = ('Use Staff', 'use staff', 'Use staff', 'use Staff'),
    )

    game_state['commands']['Use Cloak'] = Command(
        name = 'Use Cloak',
        valid_choices = ('Use Cloak', 'use cloak', 'Use cloak', 'use Cloak'),
    )

    entrance_hall()


def look_converter(look_choice):
    global game_state
    for door in game_state['room']['doors']:
        if look_choice in game_state['room']['doors'][door].valid_choices:
            print '\n', game_state['room']['doors'][door].glance
            closer = raw_input('\nWould you like to look closer?\n> ').lower()

            if closer in game_state['commands']['Yes'].valid_choices:
                print game_state['room']['doors'][door].description
                return

            elif closer in game_state['commands']['No'].valid_choices:
                print '\nAlright back to it then.'
                return

            elif closer in game_state['commands']['Back'].valid_choices:
                print '\nGuess you don\'t need to look at anything, back to it.'
                return

            else:
                print '\nThat is not very helpful. Why don\'t you try \
something like yes or no?'
                return

    for item in game_state['room']['items']:
        if look_choice in game_state['room']['items'][item].valid_choices:
            print '\n', game_state['room']['items'][item].item_look
            closer = raw_input('\nWould you like to look closer?\n> ').lower()

            if closer in game_state['commands']['Yes'].valid_choices:
                print game_state['room']['items'][item].description
                return

            elif closer in game_state['commands']['No'].valid_choices:
                print '\nAlright back to it then.'
                return

            elif closer in game_state['commands']['Back'].valid_choices:
                print '\nGuess you don\'t need to look at anything, back to it.'
                return

            else:
                print '\nThat is not very helpful. Why don\'t you try \
    something like yes or no?'
                return

    if look_choice in game_state['room']['enemies']['valid_choices']:
        print '\n', game_state['room']['enemies']['description']


    elif look_choice in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t need to look at anything, back to it.'


    else:
        print '\nThat is not helpful! next time try looking at something \
in the room or just go back...'


def pickup_converter(pickup):
    global game_state
    for item in game_state['room']['items']:
        if pickup in game_state['room']['items'][item].valid_choices:

            if not game_state['player']['inventory']:
                if item in game_state['room']['items']:
                    game_state['player']['inventory'][item] = game_state['room']['items'][item]
                    print game_state['room']['items'][item].take_me
                    print 'You picked up %s, it has been added to your \
inventory!' % game_state['room']['items'][item].name
                    return

            else:
                if item in game_state['starting_items'] and game_state['player']['inventory']:
                        print '\nYou have chosen your path!'
                        print 'Only one may be taken, move along!'
                        return

                elif item in game_state['player']['inventory'][item].valid_choices:
                    print 'You already have that.'
                    return

                elif item in game_state['room']['items']:
                    game_state['player']['inventory'][item] = game_state['room']['items'][item]
                    print game_state['room']['items'][item].take_me
                    print 'You picked up %s, it has been added to your \
inventory' % game_state['room']['items'][item].name
                    return

        elif pickup in game_state['commands']['Back'].valid_choices:
            print '\nGuess you don\'t want any of this junk, back to it.'
            return

    print """
Either You can't take that in which case you
should try something else, maybe 'the item'.

OR that is not actually a thing here and your just crazy!"""


def listen_converter(listen):
    global game_state
    for door in game_state['room']['doors']:
        if listen in game_state['room']['doors'][door].valid_choices:
            print '\n', game_state['room']['doors'][door].listen
            return

    if listen in roomlisten:
        print '\n', game_state['room']['listen']


    elif listen in game_state['room']['enemies']['valid_choices']:
        print '\n', game_state['room']['enemies']['listen']


    elif listen in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t want to hear anything then, back to it.'


    else:
        print '\nWhat ever your trying to listen to either is not in this \
room or your just crazy.'


def entry_converter(enter):
    global game_state
    for door in game_state['room']['doors']:
        if enter in game_state['room']['doors'][door].valid_choices:
            game_state['room']['doors'][door].enter()
            return

    if enter in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t want to go anywhere yet, back to it.'
        return None

    else:
        print ('\nEither that isn\'t a door, isn\'t in this room, or your just crazy!')
        return None


def ineract_converter(interact):
    global game_state
    global game_over
    for interaction in game_state['commands']:
        if interact in game_state['commands'][interaction].valid_choices:
            if interact in game_state['commands']['Use Sword'].valid_choices and 'Sword' in game_state['player']['inventory']:
                Enemy.weapon = 'sword'
                Enemy.kill_or_die()

            elif interact in game_state['commands']['Use Sword'].valid_choices and 'Sword' not in game_state['player']['inventory']:
                game_over = True

            elif interact in game_state['commands']['Use Staff'].valid_choices and 'Staff' in game_state['player']['inventory']:
                Enemy.weapon = 'staff'
                Enemy.kill_or_die()

            elif interact in game_state['commands']['Use Staff'].valid_choices and 'Staff' not in game_state['player']['inventory']:
                game_over = True

            elif interact in game_state['commands']['Use Cloak'].valid_choices and 'Cloak' in game_state['player']['inventory']:
                Enemy.weapon = 'cloak'
                Enemy.kill_or_die()

            elif interact in game_state['commands']['Use Cloak'].valid_choices and 'Cloak' not in game_state['player']['inventory']:
                game_over = True

    if interact in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t want anything to do with this thing.'
        print 'Back to it then!'
        return

    else:
        print '\nYou tried to do something, I am not really sure what.'
        print 'Whatever it was just got you killed though.'
        game_over = True
        return


def command_prompt(yes_no):
    if yes_no in game_state['commands']['Yes'].valid_choices:
        commands = raw_input('\nWhat command would you like to see options for?\n> ')
        for command in game_state['commands']:
            if commands in game_state['commands'][command].valid_choices:
                print '\n', game_state['commands'][command].valid_choices

            elif yes_no in game_state['commands']['Back'].valid_choices:
                print '\nGuess you got what you need.'

            else:
                print '\nCan\'t you read a list silly?'
                return

    elif yes_no in game_state['commands']['No'].valid_choices:
        print '\nGuess you got what you need.'

    elif yes_no in game_state['commands']['Back'].valid_choices:
        print '\nGuess you got what you need.'

    else:
        print '\nThat does not work here, try a yes or no next time.'


def quit(yes_no):
    global game_over
    if yes_no in (game_state['commands']['Yes'].valid_choices):
        exit('\nGood Bye!\n')

    elif yes_no in (game_state['commands']['No'].valid_choices):
        print '\nAlright back to the game then!'

    elif yes_no in game_state['commands']['Back'].valid_choices:
        print '\nAlright back to the game then!'

    else:
        print '\nIt\'s a simple yes or no question...'
        print 'You know what, just die instead!'
        game_state['dead'] = ('Stupidity was your end.')
        game_over = True


def action():
    global game_over
    global victory
    global game_state
    global no_enemy
    global unburnt
    global dragon
    while game_over == False:
        choice = raw_input('\nWhat action would you like to take?\n> ')

        if choice in game_state['commands']['Look'].valid_choices:
            look_converter(raw_input('\nWhat would you like to look at?\n> '))

        elif choice in game_state['commands']['Take'].valid_choices:
            pickup_converter(raw_input('\nWhat would you like to take?\n> '))

        elif choice in game_state['commands']['Listen'].valid_choices:
            listen_converter(raw_input('\nWhat would you like to listen to?\n> '))

        elif choice in game_state['commands']['Enter'].valid_choices:
            new_room = entry_converter(raw_input('\nWhich door would you \
like to enter?\n> ').lower())
            if new_room:
                new_room()

        elif choice in game_state['commands']['Interact'].valid_choices:
            if no_enemy == False:
                ineract_converter(raw_input('\nHow would you like to interact \
with this creature?\n> '))
            elif no_enemy == True:
                print '\nThere isn\'t anything to interact with here.'

        elif choice in game_state['commands']['Help'].valid_choices:
            print '\nThings you can do: \n'
            for key in game_state['commands'].keys():
                print(key)
            command_prompt(raw_input('\nWould you like to see a list of input \
options for one of these?\n> ').lower())

        elif choice in game_state['commands']['Inventory'].valid_choices:
            if game_state['player']['inventory'] == {}:
                print 'Your inventory is empty.'
            else:
                print game_state['player']['inventory']

        elif choice in game_state['commands']['Die'].valid_choices:
            if dragon and unburnt:
                game_state['dead'] = 'You decide to die here but there is a \
dragon, it tries to toast you but fails so it decides to eat you instead!'
                game_over = True

            elif dragon:
                game_state['dead'] = 'You decide to die here but there is a dragon, \
it toasts you alive like a human shaped marshmallow! Chewy.'
                game_over = True

            else:
                game_state['dead'] = '\nI don\'t know why but you chose to die, \
your neck snaps.'
                game_over = True

        elif choice in game_state['commands']['Quit'].valid_choices:
            quit(raw_input('\nAre you sure you would like to quit?\n> ').lower())

        else:
            print '\nThat is not very helpful. Look around or something! Or ask for help?'

    if victory:
        print 'You have slain the dragon and escaped the dungeon!'
        print 'Congratulations on your successful journey!'
        print 'You claim your riches and retire to a grand castle!'
        print '\n\nVICTORY!\n'
        play_again = raw_input('Would you like to play again?\n> ')
        if play_again in game_state['commands']['Yes'].valid_choices:
            new_game()
        elif play_again in game_state['commands']['No'].valid_choices:
            exit('\nGood Game!\n')
        else:
            print 'I will take that as a no.'
            exit('\nGood Bye!\n')
    else:
        print '\n', game_state['dead'], 'You have died!'
        print '\n\nGAME OVER!\n'
        play_again = raw_input('\nWould you like to play again?\n> ')
        if play_again in game_state['commands']['Yes'].valid_choices:
            new_game()
        elif play_again in game_state['commands']['No'].valid_choices:
            exit('\nGood Bye!\n')
        else:
            print '\nI will take that as a no.'
            exit('\nGood Bye!\n')


def entrance_hall():
    global game_state
    print "\n\n"
    print "-" * 80
    print """
You wake up to find yourself in a large chamber lit by torches.
Looking around you see three doors, one black, one red, and one silver.
Near each door there are three items, a cloak, a staff, and a sword.
Moving forward in the room a voice speaks to you from all around you.
'Welcome to The Trove!'
'Here you will find many things.'
'You will have only your wit, body, and the treasures of The Trove to depend on...'
'Make your choices wisely as your fate is in your own hands.'
'Will you find the path to freedom or fail as so many who came before...'

For now you may do a few things:
Use enter to go through doors.
Use listen to hear the room or behind a door.
Use take to pick up items.
Use look to examine things like the items or doors.
Anything you pick up will go into your Inventory.
Use back to make a different choice.
Or use Help if you get stuck.

'Now go!'
"""

    game_state['room']['doors']['Black door'] = Door(
        name = 'A Black door',
        listen = 'Listening at the Black door you hear only the slightest, \
quietest breath of wind and a dull deep set of rumblings, one near and one far.',
        glance = 'The Black door is so dark you have a hard \
time telling it is even there.',
        description = """
Looking closer the surface is wood but stained a darker color than anything \
you have ever seen.
Looking away your eyes have to re-adjust to the light of the room as if you \
had been in a dark space.
""",
        enter = troll_room,
        valid_choices = ('black door', 'the black door', 'a black door'),
)

    game_state['room']['doors']['Red door'] = Door(
        name = 'A Red door',
        listen = 'Listening at the Red door you hear the crackle of fire, \
as if from more torches and a deep distant rumble.',
        glance = 'The Red door is an ever changing color, as if the door it \
self was on fire.',
        description = """
The door shifts from deep blood reds to bright orange and yellow hues before \
your eyes.
It is warm to the touch and you start sweating a little just standing in \
front of it.
""",
        enter = lava_room,
        valid_choices = ('red door', 'the red door', 'a red door'),
)

    game_state['room']['doors']['Silver door'] = Door(
        name = 'A Silver door',
        listen = 'Listening at the Silver door you hear running water, \
an odd giggling, and a very faint, very distant rumbling',
        glance = 'The Silver door is made of bright metal.',
        description = """
It appears to be made of a forged material, the likes of which you have
never seen before, you doubt even a ram could damage this door.
\nIt is cool to the touch and when you pull your hand away you find your
heart beating from what you can only describe as a thrill?
""",
        enter = goblin_room,
        valid_choices = ('silver door', 'the silver door', 'a silver door'),
)

    game_state['room']['items']['Staff'] = Item(
        name = 'The Staff of Power',
        item_look = 'A tall, straight staff with twisting wood calmly set before you.',
        description = """
The Staff is tall and twisted, \
made of a deep dark wood and topped with an ever changing crystal.
It exudes power, pulsing and searing against the air.
""",
        take_me = """
The torches blaze up, wind howles through the room \
and lightning strikes the crystal atop it!
""",
        valid_choices = ('Staff', 'staff', 'A Staff', 'a Staff', 'A staff',
'a staff', 'The Staff', 'the Staff', 'The staff', 'the staff'),
)

    game_state['room']['items']['Sword'] = Item(
        name = 'Sanguineus',
        item_look = '\nA bright blade laying bare in front of the metal door.',
        description = """
The Sword is double edged and roughly three feet long, and
oddly light for its size, it has intricit etchings on either side \
of the blades face.
Even with the fine detail their isn't a single blemish on it,
you get the feeling you couldn't break it if you tried.""",
        take_me = """
You lift the sword from the ground and the blade almost seems to hum \
in your hand.
You marvel at how well balanced it is and how natural it fits \
your hand.
It feels as though it were made just for you.
You look down to find a sheath has appeared on you hip which \
you slide your new weapon into.
It's a perfect fit, but why wouldn't it be.
""",
        valid_choices = ('Sword', 'sword', 'A Sword', 'a Sword', 'A sword',
'a sword', 'The Sword', 'the Sword', 'The sword', 'the sword'),
)

    game_state['room']['items']['Cloak'] = Item(
        name = 'Nigh',
        item_look = 'A dark cloak laying losely tossed on the ground.',
        description = """
The Cloak is cool and warm, black and shimmering like a moon lit pool, \
while also all colors at once.
At times you can't even really see it.
Looking at it is a bit unnerving while also calming, it almost feels protective.
The cloth is untarnished, softer than a shadow, and carries the \
faintest smell of the first leaves of fall.
""",
        take_me = """
You pick up the cloak and wrap yourself in it.
The cloth catches wind and rustles around you.
As it settles it seems the sounds around you are clearer,
while your breathing and movement seems hushed and almost not even there.
""",
        valid_choices = ('Cloak', 'cloak', 'A Cloak', 'a Cloak', 'A cloak',
    'a cloak', 'The Cloak', 'the Cloak', 'The cloak', 'the cloak'),
)

    game_state['room']['listen'] = 'Listening to the room you hear the \
torches crackling and a subtle thruming,\nas if the very air is vibrating.'

    game_state['starting_items'] = ('Staff', 'staff', 'A Staff', 'a Staff',
'A staff', 'a staff', 'The Staff', 'the Staff', 'The staff', 'the staff',
'Sword', 'sword', 'A Sword', 'a Sword', 'A sword', 'a sword', 'The Sword',
'the Sword', 'The sword', 'the sword', 'Cloak', 'cloak', 'A Cloak', 'a Cloak',
'A cloak', 'a cloak', 'The Cloak', 'the Cloak', 'The cloak', 'the cloak')

    action()

def troll_room():
    global game_state
    global no_enemy
    print "\n\n"
    print "-" * 80
    print """
Hi
    """
    no_enemy = False

    troll = Enemy(
        name = 'Troll',
        description = ' ',
        listen = ' ',
        Sword = 'die',
        Staff = 'die',
        Cloak = 'slay',
        slay_txt = '',
        die_txt = '',
        item = '',
        item_txt = '',
        valid_choices = ('', '', ''),
        weapon = ''
    )
    troll.write()

    action()

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
