

# Establish Empty List for Rooms
room_list = []

# Establish Room Variable with 5 elements:
# Name of Room, Room to North, Room to East, Room to South, Room to West

room = ["You are in a small bedroom. There is another door to the north, and a hall to the east.\n", 3, 1, None, None]

room_list.append(room)

room = ["You are at the end of a long hallway. The moonlight is shining through the large windowed doors to the north\n"
        "and there is a large dining room to the east.\n", 4, 2, None, 0]

room_list.append(room)

room = ["You are in an large dining room, full of ornate fixtures. The room is eerily still.\nThe door to the kitchen"
        " is cracked open to the north.\n", 5, None, None, 1]

room_list.append(room)

room = ["You've reached a master bedroom, with the curtains drawn and a small candle lit on the wooden nightstand.\n"
        "There is a door to the south.\n", None, 4, 0, None]

room_list.append(room)

room = ["Now at the far end of the hall, you can see the large glass panes of the door leading out to a balcony\n"
        "overlooking the moonlit countryside to north.\n", 6, 5, 1, 3]

room_list.append(room)

room = ["This is the kitchen, and it hasn't looked used in ages. Iron pans and rusty utensils cover the counters\nas if"
        " they were searching for something.\n", None, None, 2, 4]

room_list.append(room)

room = ["The air is cold for a summer night, and the breeze picks up in a drowning howl.\nThere is a "
        "strange stillness in everything besides the pine trees lining the front of the lawn.\n"
        "You hear a door slam to the south.\n", None, None, 4, None]

room_list.append(room)

# Current Room Variable

current_room = 0

# ------------- Start Printing Game ---------------------

done = False

while not done:
    print()
    print(room_list[current_room][0])

    response = input("Which direction would you like to go?: ")

    if response.upper() == "NORTH" or response.upper() == "N":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("\nYou can't go that way...")
        else:
            current_room = next_room

    elif response.upper() == "EAST" or response.upper() == "E":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("\nYou can't go that way...")
        else:
            current_room = next_room

    elif response.upper() == "SOUTH" or response.upper() == "S":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("\nYou can't go that way...")
        else:
            current_room = next_room

    elif response.upper() == "WEST" or response.upper() == "W":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("\nYou can't go that way...")
        else:
            current_room = next_room

    elif response.upper() == "QUIT" or response.upper() == "Q":
        print("\nYou may never know why you were here...\n")
        done = True



