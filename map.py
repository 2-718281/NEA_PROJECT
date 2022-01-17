import numpy as np
import pygame as pg
import random
import random as rd

DEFAULT_ROOM_TYPE = 0
DEFAULT_ROOM_WIDTH = 30
DEFAULT_ROOM_HEIGHT = 30

TRAP_TRUE_PROBABILITY = 0.5


class Room:
    _next_room_ID = 0
    _room_dict = {}

    def __init__(self):
        self.room_type = DEFAULT_ROOM_TYPE
        self.room_height = DEFAULT_ROOM_WIDTH
        self.room_width = DEFAULT_ROOM_HEIGHT
        self.d_room_config = np.zeros((self.room_width, self.room_height))

        self.room_config = self.d_room_config
        self.floor = np.ones((self.room_width, 1))
        self.room_ID = Room._next_room_ID
        Room._next_room_ID += 1

    def default_generation(self, room_type):  # Generate room base on the type of room

        if room_type == 1:  # Setup a starting point at the 2nd row, break wall at last row
            room = self.room_config

            room[0] = self.floor
            room[self.room_width] = self.floor
            room = room.T
            room[0] = self.floor
            room = room.T

        elif room_type == 2:  # break wall and 1st and last row
            room = self.room_condig
            floor = np.ones(self.room_width, 1)
            room[0] = floor
            room[self.room_width] = floor

        elif room_type == 3:  # break 1st wall, setup a destination at 2nd last row
            room = self.room_config
            floor = np.ones(self.room_width, 1)
            room[0] = floor
            room[self.room_width] = floor
            room = room.T
            room[self.room_height] = floor
            room = room.T

        return room

    def new_room(self, room_type):  # Generate a new room

        new_room = self.default_generation(room_type)
        self.room_config = new_room
        Room._room_dict[self.room_ID] = self.room_config  # add new room to the room dictionary

    def room_update(self):
        pass

    def platfrom_generation(self):  # put new platform onto a blank array, then do a AND operation
        room_area = self.room_height * self.room_width
        for i in range(0, self.room_height):
            if room_area < 0.5(self.room_width * self.room_height):
                length = rd.randint(0, self.room_width)
                start_pos = rd.randint(0, self.room_width - length)
                new_plat = np.ones(self.length,1)
                
            else:
                pass

    def trap_generation(self):  # generate trap upon platform
        for i in self.room_config:
            for j in self.room_config[i]:
                if j == 1:
                    chance = random.Random   # there is a 50% chance of generating 1 trap
                    if chance >= TRAP_TRUE_PROBABILITY:
                        pass
                    else:
                        self.room_config = 2  # 2 represent trap

    def validation_check(self):  # check if there is at least 1 valid route
        pass



