# test terminal UI
# UI gets items from save json file.
import keyboard
import time
from Map import room


class UI:

    def __init__(self):
        self.clock = 30

    def render_map(self, map):  # render map background

        for i in range(map.shape[0]):
            print_str = ''
            for j in range(map.shape[1]):
                if map[i, j] == 1:
                    print_str += '#'
                elif map[i, j] == 2:
                    print_str += 'T'
                elif map[i, j] == 3:
                    print_str += ''
                elif map[i, j] == 4:
                    print_str += 'S'
                elif map[i, j] == 5:
                    print_str += 'E'
                else:
                    print_str += " "

            print(print_str)


e = UI()
e.render_map(room.Room.generate_map())
