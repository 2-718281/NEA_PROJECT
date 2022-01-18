import numpy as np
import random as rd
import constant as c


class Room:
    # tile 0 == empty, 1 == solid platform, 2 == trap platform, 3 == , 4 == spawning tile, 5 == destination tile
    _next_room_ID = 0
    _room_dict = {}

    def __init__(self, room_width=c.DEFAULT_ROOM_WIDTH, room_height=c.DEFAULT_ROOM_HEIGHT,
                 room_type=c.DEFAULT_ROOM_TYPE):
        self.room_type = room_type
        self.room_height = room_height
        self.room_width = room_width
        self.d_room_config = np.zeros((room_height, room_width))  # type 0 rooms : are filled with many 0s

        self.room_config = self.d_room_config.copy()  # copy the default room 0 to new room template
        self.room_ID = Room._next_room_ID
        self._platform_dict = {}
        # self.room_area = self.room_width * self.room_height  replaced by the calc_area function
        Room._next_room_ID += 1

        self.new_room(room_type)  # generate new room object

    def default_generation(self, room_type):  # Generate room base on the type of room :1,2,3
        room = self.d_room_config.copy()
        if room_type == 1:  # Setup a starting point at the 2nd row, break wall at last row
            room[0, :] = 1
            room[self.room_height - 1, :] = 1
            room[:, 0] = 1
            room[self.room_height - 2, 1] = 4

        elif room_type == 2:  # a tube like room
            room[0, :] = 1
            room[self.room_height - 1, :] = 1

        elif room_type == 3:  # setup a destination at 2nd last row
            room[0, :] = 1
            room[self.room_height - 1, :] = 1
            room[:, self.room_width - 1] = 1
            room[self.room_height - 2, self.room_width - 2] = 5
        return room

    def new_room(self, room_type):  # Generate a new room

        self.room_config = self.default_generation(room_type)
        self.platfrom_generation()
        self.trap_generation()
        Room._room_dict[self.room_ID] = self.room_config  # add new room to the room dictionary

    def calc_room_area(self):
        return np.sum((self.room_config == 0).astype(np.int32))  # sum up all None-0 cells to work out area

    def platfrom_generation(self):  # put solid platform into the room
        print("generating platform")
        candidate_platform_number = rd.randint(self.room_height // 2, self.room_height - 1)
        # random numbers of platform

        for i in range(0, candidate_platform_number):
            room_area = self.calc_room_area()

            if room_area > 0.6 * (self.room_width * self.room_height):

                for k in range(5):  # try max 5 times
                    length = rd.randint(3, self.room_width // 2)
                    start_pos_x = rd.randint(1, self.room_width - length - 2)
                    center_pos_x = start_pos_x + length // 2
                    center_pos_y = rd.randint(1, self.room_height - 2)
                    result = Room.validation_check(self.room_config, [center_pos_x, center_pos_y], length, radius=2)

                    if result:
                        self.room_config[center_pos_y, start_pos_x:start_pos_x + length] = 1
                        self._platform_dict[len(self._platform_dict)] = (length, center_pos_x, center_pos_y)
                        print('platform added')
                        break
            else:
                break

    def trap_generation(self):  # generate trap upon platform
        print("generate traps")
        for i in range(1, self.room_height - 1):
            for j in range(1, self.room_width - 1):
                if self.room_config[i][j] == 1:
                    chance = rd.random()  # there is a 50% chance of generating 1 trap
                    if chance < c.TRAP_TRUE_PROBABILITY:
                        self.room_config[i][j] = 2

    @staticmethod
    def validation_check(candidate_map, center_pos, platform_length,
                         radius=3):  # check if there is at least 1 valid route
        roi_left = max(0, center_pos[0] - platform_length // 2 - radius)
        roi_right = min(candidate_map.shape[1], center_pos[0] + platform_length // 2 + radius + 1)
        roi_down = max(0, center_pos[1] - radius)
        roi_up = min(candidate_map.shape[0], center_pos[1] + radius + 1)

        count_occupied = np.sum((candidate_map[roi_down:roi_up, roi_left:roi_right] > 0).astype(np.int32))
        # print(count_occupied)
        return count_occupied == 0

    @staticmethod
    def room_dict_getter():
        return Room._room_dict
