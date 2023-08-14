# Thais DeOliveira
# 04/24/22
# The program is a text game with a haunted house theme. The user moves through the house collecting items to rid
# the house of the ghost. To win the game, the player must collect all the items before reaching it. If the
# player reaches the room with the ghost before collecting all the items, the player loses.

# Imported the time module for output delays using the "sleep()" method.
import time

# A dictionary containing each room on the map as keys. Their values are nested dictionaries containing the command
# keys that correspond to available commands that can be performed in each room.
rooms = {
    "the piano room": {"go east": "the living room"},
    "the living room": {"go west": "the piano room", "go east": "the doll room", "go north": "the kitchen",
                        "go south": "the library", "item": "flashlight"},
    "the kitchen": {"go south": "the living room", "go east": "the basement", "item": "salt"},
    "the basement": {"go west": "the kitchen", "item": "holy water"},
    "the library": {"go east": "the bedroom", "go north": "the living room", "item": "holy bible"},
    "the bedroom": {"go west": "the library", "item": "ghost"},
    "the doll room": {"go west": "the living room", "go north": "the children's room", "item": "prayer beads"},
    "the children's room": {"go south": "the doll room", "item": "cross"}
        }

# Creates a hardcoded list of the valid commands.
command_list = ["go north", "go east", "go west", "go south", "grab item", "commands"]

# These print statements introduce the player to the game. They are formatted for readability.
print("\n{:25}{start}".format(' ', start="Haunted House Text Game"))
print("\"A family is being viciously haunted by a dangerous poltergeist. It is up to you,")
print("a well-known exorcist, to cleanse the spirit and allow it to move on!\"")
time.sleep(4)
print("\nMove through each room of the house carefully. There are 8 rooms containing 6 items and 1 ghost.")
print("Collect all 6 items to exorcise the ghost. However, if you run into the violent spirit before")
print("collecting all 6 items, it's GAME OVER!!\n")
print("It's all up to you now. Good Luck!!!\n")
time.sleep(12)


# this function prints the command list for the user when called.
def move_list():
    for commands in command_list:             # Loops through command list, printing each element, indented + uppercase.
        print("\t-{}".format(commands.upper()))

# This block introduces the player to the command list and signals the start of the game.
# It also initializes the "command" variable to an empty value, the "current_room" variable to the starting room and
# the "inventory[]" list as an empty set.
print("The list of valid commands are as follows:")
move_list()                                     # calls the "move_list()" function to print the command list
print("\nGood luck and have fun!\n\nYOU ENTER THE HAUNTED HOUSE....")
time.sleep(3)
command = ""
current_room = "the piano room"
inventory = []


# This function is called when the player loses the game. It prints a message showing that the player has lost.
def lost_game():
    print("BOO!!!!")
    print("""
     .-----.
   .'  \\ /  '.
  /  .-. .-.  \\
  |  | | | |  |
  \\  \\o/ \\o/ /
  _/    ^    \\_
 | \\  ,---,  / |
 / /`--. .--`\\ \\
/ /'---` `---'\\ \\
'.__.       .__.'
    `|     |`
     |     \\
     \\      '--.
      '.        `\\
        `'---.   |
           ,__) /
            `..' """)
    print("OH NO!! You got taken by the ghost!\nSorry, better luck next time!")


# This function is called when the player wins the game. It prints a message showing that the player has won.
def won_game():
    print("VICTORY!!")
    print("""
           ,
        .--')
       /    /
      |    /
   /`.\\   (_.'\\
   \\          /
    '--. .---'
      ( " )
       '-'
       """)
    print("You've defeated the ghost! Congratulations!")


# This function shows the status of the player to the user. It prints what room the player is in, if the room contains
# the ghost, if that room has an item, and prints the inventory list for the player. If the room contains the ghost,
# the function returns a value to signal the end of the game.
def player_status():
    if "item" in rooms[current_room] and rooms[current_room]["item"] != "ghost":
        print("\nYou have entered the {}. It contains the {}.".format(current_room.upper(),
                                                                      rooms[current_room]["item"].upper()))
    elif "item" in rooms[current_room] and rooms[current_room]["item"] == "ghost":
        if len(inventory) < 6:
            time.sleep(1)
            lost_game()                        # Calls the "lost_game()" function if the inventory list is not full.
            return 0                           # Returns 0 to end the game.
        else:
            time.sleep(1)
            won_game()                         # Calls the "won_game()" if the inventory list is full.
            return 0                           # Returns 0 to end the game.
    else:
        print("\nYou have entered the {}. It does not contain an item.".format(current_room.upper()))
    print("Current Inventory list: {} {}/6".format(inventory, len(inventory)))


# This function uses the command from the user as an argument when called. The parameter is the "move" the player wants
# to make.
    # If the player inputs a valid direction, the player is moved to the next room.
    # If the player enters an invalid direction, it displays a message that the player cannot go that way.
    # If the player enters a command to grab an item, it adds the item to the inventory list by popping the item value
            # from the nested dictionary for the current room and appends it to the "inventory[]" list.
    # The player can also enter a command to see the list of commands. This action calls the "move_list()" function.
    # If the player's input is not on the command list, a message is displayed that it's not a valid command and calls
            # the "move_list()" function.
def make_move(move):
    global current_room                                 # The value of the variable "current_room" is changed to the
    if move in rooms[current_room]:                     # value that corresponds to the command in the nested dict.
        current_room = rooms[current_room][move]
    elif move not in rooms[current_room] and move in command_list:
        if move == "grab item":
            if "item" in rooms[current_room]:
                inventory.append(rooms[current_room].pop("item"))            # Grabs item if there is one.
            else:
                print("There are currently no items in this room to grab.")  # If there's no item, displays message.
        elif move == "commands":
            move_list()
        else:
            print("\nCan't go that way! Try again!\n")
            time.sleep(2)
    else:
        print("\nThat's not a valid command...")
        move_list()
        time.sleep(2)
        print("\nTry again.")


# This block loops by first calling the "player_status()" function. It then prints a prompt for the user's next move.
# Once the "command" variable is set, the "make_move()" function is called. The loop is infinite until the
# "player_status()" function returns a value.
time.sleep(6)
while True:
    if player_status() == 0:                    # Calls the "player_status()" function. If the return value of the
        break                                   # function is equal to 0, then the loop breaks and the game ends.
    print("{line:*<25} <(`o`<)".format(current_room.upper(), line='(>`o`)> '))
    command = input("What will you do?\n").lower().strip()  # Sets value of "command" variable to user input
    make_move(command)                                      # Calls the "make_move()" function. Uses the set value
                                                            # of the "command" variable as the argument.

# Exited loop and game is over. Prints exit statements.
print("Game Over. Thanks for playing!")
print("^(^_^)> ************** <(^_^)^")
