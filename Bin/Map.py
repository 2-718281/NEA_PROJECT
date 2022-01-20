import random as rd
from room import Room
from Tools import constant as c
import numpy as np


def merge_map():
    room_amount = rd.randint(c.MIN_ROOM, c.MAX_ROOM)
    new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=1)
    for i in range(0, room_amount + 1):
        new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=2)
    new_room = Room(room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT, room_type=3)

    room_lst = Room.room_dict_to_list()
    merged_map = np.hstack(list(room_lst))

    return merged_map

# export the merged map to a txt file, if file exist, overwrite the old map.
merge_map()