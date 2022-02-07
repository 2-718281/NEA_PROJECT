import pygame as pg
from content.Tools import constant as c


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, h, w, index):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(c.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = index


class Starting(pg.sprite.Sprite):
    def __init__(self,x ,y ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((c.ROOM_TO_GUI_SCALE,c.ROOM_TO_GUI_SCALE))
        self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Trap(pg.sprite.Sprite):
    def __init__(self,x ,y ):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((c.ROOM_TO_GUI_SCALE,c.ROOM_TO_GUI_SCALE))
        self.image.fill(c.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y