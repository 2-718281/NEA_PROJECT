# GUI file
# render everything
import pygame as pg
from content.Tools import constant as c


class GUI:
    def __init__(self, w, h):
        pg.init()
        self.clock = pg.time.Clock()  # clock_init
        self.screen = pg.display.set_mode((w, h))  # window size
        self.font_name = pg.font.match_font(c.FONT_NAME)

        # layer that move with the camera
        self.background = pg.image.load(c.BACKGROUND)
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, (int(self.background_rect.width / 1.33), int(self.background_rect.height / 1.33)))

        # camera
        self.game_camera = pg.display.set_mode((c.WIDTH, c.HEIGHT)).get_rect()
        self.game_ground = pg.Surface((self.background_rect.width, self.background_rect.height))
        pg.display.set_caption(c.TITLE)  # 初始化标题

        self.state = 'START'


    def main_game(self):
        pass

    def pause_menu(self):
        pass

    def check_state(self):
        pass

    def draw_text(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)