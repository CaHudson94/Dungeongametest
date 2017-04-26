#ex 36 and 43
#Each room needs:
#Doors, Items, Enemy, list of contents, a listen, and a 'dead' if you want.
#Need to move rooms to seperate files and import as modules
from sys import exit

game_state = {}
dragon = None
unburnt = None
victory = None
game_over = None
no_enemy = None
enemy_alive = None
room_contents = None
entries = 0

door = ( 'door', 'the door', 'doors', 'the doors')
item = ('item', 'items')
room = ('room', 'the room')

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
    global enemy_alive

    def __init__(self, name, description, listen, Sword, Staff, Cloak,
    slay_txt, die_txt, item_txt, door_clear, valid_choices):
        self.name = name
        self.description = description
        self.listen = listen
        self.Sword = Sword
        self.Staff = Staff
        self.Cloak = Cloak
        self.slay_text = slay_txt
        self.die_text = die_txt
        self.item_txt = item_txt
        self.door_clear = door_clear
        self.valid_choices = valid_choices

    def dead(self):
        game_state['dead'] = [self.die_text]

    def slay(self):
        enemy_alive = False
        print self.slay_text
        print self.item_txt
        print self.door_clear


def new_game():
    global game_state
    global dragon
    global unburnt
    global victory
    global game_over
    global no_enemy
    global enemy_alive
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
            'enemies': {},
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

    enemy_alive = False

    game_state['commands']['Look'] = Command(
        name = 'Look',
        valid_choices = ('look', 'l', 'lo'),
    )

    game_state['commands']['Take'] = Command(
        name = 'Take',
        valid_choices = ('take', 't'),
    )

    game_state['commands']['Listen'] = Command(
        name = 'Listen',
        valid_choices = ('listen', 'lis',),
    )

    game_state['commands']['Enter'] = Command(
        name = 'Enter',
        valid_choices = ('enter', 'e'),
    )

    game_state['commands']['Help'] = Command(
        name = 'Help',
        valid_choices = ('help', 'h'),
    )

    game_state['commands']['Back'] = Command(
        name = 'Back',
        valid_choices = ('back', 'b'),
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
        valid_choices = ('die', 'i die', 'dead'),
    )

    game_state['commands']['Inventory'] = Command(
        name = 'Inventory',
        valid_choices = ('inventory', 'i', 'inv'),
    )

    game_state['commands']['Quit'] = Command(
        name = 'Quit',
        valid_choices = ('quit', 'q'),
    )

    game_state['commands']['Interact'] = Command(
        name = 'Interact',
        valid_choices = ('int', 'in', 'interact'),
    )

    game_state['commands']['Use Sword'] = Command(
        name = 'Use Sword',
        valid_choices = ('use sword', 'use the sword'),
    )

    game_state['commands']['Use Staff'] = Command(
        name = 'Use Staff',
        valid_choices = ('use staff', 'use the staff'),
    )

    game_state['commands']['Use Cloak'] = Command(
        name = 'Use Cloak',
        valid_choices = ('use cloak', 'use the cloak'),
    )

    entrance_hall()


def look_converter(look_choice):
    global game_state
    for door in game_state['room']['doors']:
        if look_choice in game_state['room']['doors'][door].valid_choices:
            print game_state['room']['doors'][door].glance
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
            print game_state['room']['items'][item].item_look
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

    for enemy in game_state['room']['enemies']:
        if look_choice in game_state['room']['enemies'][enemy].valid_choices:
            print game_state['room']['enemies'][enemy].description


    if look_choice in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t need to look at anything, back to it.'


    else:
        print '\nThat is not helpful! next time try looking at something \
in the room or just go back...'


def pickup_converter(pickup):
    global game_state
    global room_contents
    for item in game_state['room']['items']:
        if pickup in game_state['room']['items'][item].valid_choices:

            if not game_state['player']['inventory']:
                if item in game_state['room']['items']:
                    game_state['player']['inventory'][item] = game_state['room']['items'][item]
                    print game_state['room']['items'][item].take_me
                    print 'You picked up %s, it has been added to your \
inventory!' % game_state['room']['items'][item].name
                    room_contents.remove(item)
                    return

            else:
                if item in game_state['starting_items']:
                    if game_state['player']['inventory']:
                        print '\nYou have chosen your path!'
                        print 'Only one may be taken, move along!'
                        return

                elif item in game_state['player']['inventory']:
                    print '\nYou already have that.'
                    return

                elif item in game_state['room']['items']:
                    game_state['player']['inventory'][item] = game_state['room']['items'][item]
                    print game_state['room']['items'][item].take_me
                    print 'You picked up %s, it has been added to your \
inventory!' % game_state['room']['items'][item].name
                    room_contents.remove(item)
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

    for enemy in game_state['room']['enemies']:
        if listen in game_state['room']['enemies'][enemy].valid_choices:
            print '\n', game_state['room']['enemies'][enemy].listen

    if listen in room:
        print '\n', game_state['room']['listen']


    elif listen in game_state['commands']['Back'].valid_choices:
        print '\nGuess you don\'t want to hear anything then, back to it.'


    else:
        print '\nThere are a few options here:'
        print 'You can\'t get to what you want right now,'
        print 'or whatever your trying to listen to either is not in this room,'
        print 'OR your just crazy!'


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
            if interact in game_state['commands']['Use Sword'].valid_choices:
                if 'Sword' in game_state['player']['inventory']:
                    for enemy in game_state['room']['enemies']:
                        if game_state['room']['enemies'][enemy].Sword == 'slay':
                            game_state['room']['enemies'][enemy].slay()
                            return

                        elif game_state['room']['enemies'][enemy].Sword == 'die':
                            game_over = True
                            return

                        else:
                            print game_state['room']['enemies'][enemy].Sword
                            return

                elif 'Sword' not in game_state['player']['inventory']:
                    print 'You don\'t have that this is going to end poorly.'
                    game_over = True
                    return

            elif interact in game_state['commands']['Use Staff'].valid_choices:
                if 'Staff' in game_state['player']['inventory']:
                    for enemy in game_state['room']['enemies']:
                        if game_state['room']['enemies'][enemy].Staff == 'slay':
                            game_state['room']['enemies'][enemy].slay()
                            return

                        elif game_state['room']['enemies'][enemy].Staff == 'die':
                            game_over = True
                            return

                        else:
                            print game_state['room']['enemies'][enemy].Staff
                            return

                elif 'Staff' not in game_state['player']['inventory']:
                    print 'You don\'t have that this is going to end poorly.'
                    game_over = True
                    return

            elif interact in game_state['commands']['Use Cloak'].valid_choices:
                if 'Cloak' in game_state['player']['inventory']:
                    for enemy in game_state['room']['enemies']:
                        if game_state['room']['enemies'][enemy].Cloak == 'slay':
                            game_state['room']['enemies'][enemy].slay()
                            return

                        elif game_state['room']['enemies'][enemy].Cloak == 'die':
                            game_over = True
                            return

                        else:
                            print game_state['room']['enemies'][enemy].Cloak
                            return

                elif 'Cloak' not in game_state['player']['inventory']:
                    print 'You don\'t have that this is going to end poorly.'
                    game_over = True
                    return

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
        choice = (raw_input('\nWhat command would you \
like to see options for?\n> ').lower())
        for command in game_state['commands']:
            if choice in game_state['commands'][command].valid_choices:
                print '\n', game_state['commands'][command].valid_choices
                return

            elif yes_no in game_state['commands']['Back'].valid_choices:
                print '\nGuess you got what you need.'
                return

        else:
            print '\nCan\'t you read a list silly?'


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
    global room_contents
    while game_over == False:
        choice = (raw_input('\nWhat action would you like to take?\n> ').lower())

        if choice in game_state['commands']['Look'].valid_choices:
            look_converter(raw_input('\nWhat would you like to look at?\n> ').lower())

        elif choice in game_state['commands']['Take'].valid_choices:
            pickup_converter(raw_input('\nWhat would you like to take?\n> ').lower())

        elif choice in game_state['commands']['Listen'].valid_choices:
            listen_converter(raw_input('\nWhat would you like to listen to?\n> ').lower())

        elif choice in room:
            print '\nThis room contains: \n'
            print '\n'.join(str(c) for c in room_contents)

        elif choice in game_state['commands']['Enter'].valid_choices:
            new_room = entry_converter(raw_input('\nWhich door would you \
like to enter?\n> ').lower())
            if new_room:
                new_room()

        elif choice in game_state['commands']['Interact'].valid_choices:
            if no_enemy == False:
                ineract_converter(raw_input('\nHow would you like to interact \
with this creature?\n> ').lower())
            elif no_enemy == True:
                print '\nThere isn\'t anything to interact with here.'

        elif choice in game_state['commands']['Help'].valid_choices:
            print '\nThings you can use to interact: '
            print '\ndoor: ', door
            print '\nitem: ', item
            print '\nroom: ', room
            print '\nCommands at your disposal: \n'
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
    global room_contents
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

For now, you may do a few things:
Use enter to go through doors.
Use listen to hear the room or behind a door.
Use take to pick up items.
Use look to examine things like the items or doors.
Anything you pick up will go into your Inventory.
Use back to make a different choice.
If you need to know what is in the room again use Room to see its contents.
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
Looking away your eyes must re-adjust to the light of the room as if you \
had been in a dark space.
""",
        enter = troll_room,
        valid_choices = ('black door', 'the black door', 'a black door'),
)

    game_state['room']['doors']['Red door'] = Door(
        name = 'A Red door',
        listen = 'Listening at the Red door you hear the crackle of fire, \
as if from more torches and a deep distant rumble.',
        glance = 'The Red door is an ever-changing color, as if the door it \
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
an odd giggling, and a very faint, very distant rumbling.',
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
made of a deep dark wood and topped with an ever-changing crystal.
It exudes power, pulsing and searing against the air.
""",
        take_me = """
The torches blaze up, wind howls through the room \
and lightning strikes the crystal atop it, which glows blue!
""",
        valid_choices = ('staff', 'a staff', 'the staff'),
)

    game_state['room']['items']['Sword'] = Item(
        name = 'Sanguineus',
        item_look = '\nA bright blade laying bare in front of the metal door.',
        description = """
The Sword is double edged and roughly three feet long, and
oddly light for its size, it has intricate etchings on either side \
of the blades face.
Even with the fine detail there isn't a single blemish on it,
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
        valid_choices = ('sword', 'a sword', 'the sword'),
)

    game_state['room']['items']['Cloak'] = Item(
        name = 'Nigh',
        item_look = 'A dark cloak laying losely tossed on the ground.',
        description = """
The Cloak is cool and warm, black and shimmering like a moon lit pool, \
while also all colors at once.
At times, you can't even really see it.
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
        valid_choices = ('cloak', 'a cloak', 'the cloak'),
)

    game_state['room']['listen'] = 'Listening to the room you hear the \
torches crackling and a subtle thrumming,\nas if the very air is vibrating.'

    game_state['starting_items'] = ('Staff', 'Sword', 'Cloak')

    room_contents = ['Black door', 'Red door', 'Silver door',
'Staff', 'Sword', 'Cloak']

    action()


def troll_room():
    global game_state
    global no_enemy
    global enemy_alive
    global room_contents

    game_state['room']['items'] = {}

    print "\n\n"
    print "-" * 80
    print """
You walk through the door to find yourself in a dimly lit, mid-sized chamber.
There is a single chandelier in the center of the room with only a few \
lit candles.
You notice the room smells awful for some reason and look around to find...

'A TROLL!'

'Yes, there is a troll in the dungeon.'
'I thought you ought to know.'

'Luckily for you it is sound asleep on the other side of the room.'
'Unluckily for you the only other doors out of the room are behind it's fat \
smelly butt.'

Aside from you, the dark, the smell, the troll, and the three doors the room \
is completely empty.

Oh and the door you just came through locks firmly behind you.

'As this is the first enemy you have encountered now would be a good time'
'to tell you that you can interact with them with the items from the first'
'room. You can do this simply by saying use (item) these are also commands'
'which you can still find in help.'
    """
    no_enemy = False

    enemy_alive == True

    game_state['room']['enemies']['troll'] = Enemy(
        name = 'Troll',
        description = """
A huge, smelly, creature asleep on his large butt.
He is holding a rather large club that is three times your size around and
three times your height. He is only wearing a loin cloth and an anklet
which he happens to be wearing as a ring on his pinky.
""",
        listen = 'He is just snoring and grunting a little in his sleep.',
        Sword = 'die',
        Staff = 'die',
        Cloak = 'slay',
        slay_txt = """
Using your cloak, you're able to get right in front of \
the troll without waking him up.
You jump up and kick him in the head toppling him backwards.

He wakes up briefly to find his head colliding with the ground,
swiftly follow by his own club crushing his skull killing him instantly.
        """,
        die_txt = """
Well you tried something and it was quite noisy.
So the troll woke up!
He yawns swinging his club wide...

It catches you in the gut picking you up off your feet.
The air is knocked out of you and your in agonizing pain for a brief moment...

And then you are jelly on the wall!
You were crushed between the trolls club and the wall.
""",
        item_txt = 'The clasp on the anklet opens and it falls to the ground \
with a heavy crash, cracking the stones of the floor.',
        door_clear = """
With the troll dead, brains decorating the floor, the doors are now clear.
One is a pure white and the other a plain brown.
""",
        valid_choices = ('troll', 'the troll'),
    )
    game_state['room']['enemies']['troll'].dead()

    if enemy_alive == False:
        game_state['room']['items']['Anklet'] = Item(
            name = 'Troll\'s anklet',
            item_look = 'A heavy weighted ring with a clasp.',
            description = """
The anklet is made up of a dense metal and is heavy to your hands.
There are seven small metal orbs and seven small steel octahedrons
at points around the anklet.
It seems very weighty while making you feel lighter in contrast.
""",
            take_me = """
You clasp the anklet on to yourself and a feeling rushes through you.
Your steps are lighter and fleeting while they also bear the weight \
of someone twice your size or more.
Although you are slightly louder now you seem much quicker.
You feel like you could punch through a wall.

'Probably not these ones though, given the magic here.' You think to yourself.
""",
            valid_choices = ('anklet', 'the anklet', 'troll\'s anklet'),
)

        game_state['room']['doors']['Brown door'] = Door(
            name = 'Brown door',
            listen = """
Listening at the door you hear nothing, deafening, unending nothingness.
Silence fails to describe the depth of nothingness you hear.
""",
            glance = 'A brown wood door.',
            description = 'Just a simple plain brown wood door nothing descipt \
or unique about it or it\'s handle.',
            enter = infinite_room,
            valid_choices = ('brown door', 'the brown door'),
)

        game_state['room']['doors']['White door'] = Door(
            name = 'White door',
            listen = """
You hear a single deep rumbling sound still far off though and a quite...
clicking sound?
The second sound send chills down your spine.
There is also a faint trickling sound which might be water?
""",
            glance = 'The door is pure white, a stark contrast to the dark room.',
            description = """
The door is not just white but perfectly clean even with the dank dirty nature \
of the room.
It strikes you as odd considering the layer of dirt and grim on everything else.
The grain of the wood appears to be woven some how, rather than grown or carved.
""",
            enter = spider_room,
            valid_choices = ('the white door', 'white door'),
)

        room_contents = ['Anklet', 'Brown door', 'White door']

    elif enemy_alive == True:

        room_contents = ['Troll', 'Two blocked doors']

        action()

def spider_room():

    pass


def goblin_room():

    pass


def lava_room():

    pass


def infinite_room():
    global entries
    global game_over
    entries = entries + 1
    if entries <= 9 and entries > 1:
        print '\nJust as the room before...'
    elif entries > 9:
        game_state['dead'] = """
You are trapped in this darkness, this nothingness.
You go on for a while but eventually go insane.
You carve out your own eyes.
"""
        game_over = True

    print """
You find yourself in a black room.
It is devoid of all color, life or light. It is not dark simply black.
Even so you can see a door opposite you and the door \
that has just swung shut behind you.
There is nothing here in fact the room is it self nothing.
However unlike past rooms the door you came through does not \
seem to have locked.
"""

    game_state['room']['doors']['Near brown door'] = Door(
        name = 'Near brown door',
        listen = """
Listening at the door you hear nothing, deafening, unending nothingness.
Silence fails to describe the depth of nothingness you hear.
""",
        glance = 'A brown wood door.',
        description = 'Just a simple plain brown wood door nothing descipt \
or unique about it or it\'s handle.',
        enter = infinite_room,
        valid_choices = ('the near brown door', 'near brown door'),
)

    game_state['room']['doors']['Far brown door'] = Door(
        name = 'Far brown door',
        listen = """
Listening at the door you hear nothing, deafening, unending nothingness.
Silence fails to describe the depth of nothingness you hear.
""",
        glance = 'A brown wood door.',
        description = 'Just a simple plain brown wood door nothing descipt \
or unique about it or it\'s handle.',
        enter = infinite_room,
        valid_choices = ('the far brown door', 'far brown door'),
)

    game_state['room']['doors']['Secret Door One'] = Door(
        name = 'Magic missile door',
        listen = '',
        glance = '',
        description = '',
        enter = treasure_room,
        valid_choices = ('i use magic missile',
'i use magic missile at the darkness', 'i cast magic missile',
'i cast magic missile at the darkness', 'cast magic missile',
'cast magic missile at the darkness', 'use magic missile',
'use magic missile at the darkness'),
)

    game_state['room']['doors']['Secret Door Two'] = Door(
        name = 'Name of the Empress door',
        listen = '',
        glance = '',
        description = '',
        enter = treasure_room,
        valid_choices = ('moonchild', 'moonchild!', 'name of the empress'),
)

    room_contents = ['Near brown door', 'Far brown door']

    action()



def dragon_chamber():
    dragon = True
    print " "


def treasure_room():
    print " "


new_game()
