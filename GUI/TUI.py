# test terminal UI
# UI gets items from save json file.
import keyboard
import time
from Map import room


class UI:

    def __init__(self, new_map):
        self.clock = 30
        self.state = 'start'
        self.map = new_map

    ##############################################

    # render methods
    def render_map(self):  # render map background
        for i in range(self.map.shape[0]):
            print_str = ''
            for j in range(self.map.shape[1]):
                if self.map[i, j] == 1:
                    print_str += '#'
                elif self.map[i, j] == 2:
                    print_str += 'T'
                elif self.map[i, j] == 3:
                    print_str += ''
                elif self.map[i, j] == 4:
                    print_str += 'S'
                elif self.map[i, j] == 5:
                    print_str += 'E'
                else:
                    print_str += " "

            print(print_str)

    ##############################################
    # states
    # ui states
    def playing_state(self):
        self.state = 'PLAYING'

    def pause_state(self):
        self.state = 'PAUSE'

    def level_pass_state(self):
        self.state = 'LEVEL_PASS'

    def level_failed_state(self):
        self.state = 'FAILED'

    # player states

    def dead_state(self):
        self.state = 'DEAD'

    def jump_state(self):
        self.state = 'JUMP'

    def attack_state(self):
        self.state = 'ATTACK'

    def fall_state(self):
        self.state = 'FALL'

    def damaged_state(self):
        self.state = 'DAMAGED'

