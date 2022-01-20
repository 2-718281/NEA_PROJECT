import pygame as pg
from Tools import constant as c


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, h, w, index):  # platform class
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))  # 长宽
        self.image.fill(c.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = index
