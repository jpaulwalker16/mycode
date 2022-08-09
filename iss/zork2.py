#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'west' : 'Greenhouse',
                  'item'  : 'map',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            'Greenhouse' : {
                'east' : 'Kitchen',
                'south' : 'Backyard',
                'item' : 'poison',
                },
            'Backyard' : {
                'north' : 'Greenhouse',
                'item' : 'monster',
                'east' : 'Kitchen',
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

#All rooms
for x in rooms:
    allrooms = list(rooms.keys())

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

# Give adjacant room locations


# Define hints in the game

    # you need to write out conditions fully, even if it's repetitive
    # so instead of this:

    # if currentRoom =='Garden' or 'Greenhouse'

    # make it this:

    # if currentRoom =='Garden' or currentRoom == 'Greenhouse'

    # otherwise it makes a "false true": writing just "or 'Greenhouse' is confirming if the string 'Greenhouse' exists, which it does


  if currentRoom =='Garden' or currentRoom == 'Greenhouse'  and 'key' in inventory:      print('You are on your way to the mountain of Mordor to unlock the gate of doom...find the potion to be successful in your trip!')

  elif currentRoom =='Garden' or currentRoom == 'Greenhouse' and 'map' in inventory:
       print('You are on your way to the mountain of Mordor to unlock the gate of doom...find the key and potion to be successful in your trip!')

  elif currentRoom =='Garden' or currentRoom == 'Greenhouse' and 'potion' in inventory:       print('You are on your way to the mountain of Mordor to unlock the gate of doom...find the key to be successful in your trip!')

## Define how a player can win
  elif currentRoom == 'Garden' or currentRoom == 'Greenhouse'  and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
#Footer
#© 2022 GitHub, Inc.
#Footer navigation
#Terms
#Privacy
#Security
#Status
#Docs
#Contact G
