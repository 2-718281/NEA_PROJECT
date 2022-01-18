import random as rd
from room import Room
import constant as c
import numpy as np


room_amount = rd.randint(c.MIN_ROOM, c.MAX_ROOM)
new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=1)
for i in range(0, room_amount+1):
    new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=2)
new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=3)

room_dict = Room.room_dict_getter()  # get room dictionary

