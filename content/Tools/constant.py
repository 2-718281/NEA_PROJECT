# game setting constants
FPS = 60
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
TITLE = "this is a title"
DEFAULT_IMG = 0
FONT_NAME = "arial"

# main game constants
BACKGROUND = ''

# room constants
WIDTH = 800
HEIGHT = 600
CAM_VEL = 0.5

# player constants
P_ACC = 0.5
P_FRI = -0.12
P_GRA = 0.5
P_HP = 10

# room generation constants
DEFAULT_ROOM_TYPE = 0
DEFAULT_ROOM_WIDTH = 10
DEFAULT_ROOM_HEIGHT = 10
TRAP_TRUE_PROBABILITY = 0.3
MAX_ROOM = 10
MIN_ROOM = 3

ROOM_TO_GUI_SCALE = 30

MAP_WIDTH = 4
MAP_HEIGHT = 4

PLATFORM_LIST = {(0, HEIGHT - 60, 10000, 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20), (1000, 300, 200, 10), (1500, 200, 300, 20)}
PLATFORM_LIST = [(360, 240, 40, 40), (360, 360, 40, 60), (400, 240, 40, 60), (320, 120, 40, 80), (400, 440, 40, 100)]