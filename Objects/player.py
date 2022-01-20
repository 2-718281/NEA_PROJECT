import sys
import random
import constants
import os
from constants import *

vec = pg.math.Vector2

g_F = os.path.dirname(__file__)
i_F = os.path.join(g_F, "../game/game/img")


class Player(pg.sprite.Sprite):  # inherit from sprite
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)  # 初始化sprite
        self.game = game

        # self.image = pg.image.load(os.path.join(i_F, "pl1.PNG"))  # 图片 player pic
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()  # 获取正方形 get rect
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)  # 初始化位置矢量 position vector
        self.vel = vec(0, 0)  # 初始化速度矢量 velocity vector
        self.acc = vec(0, 0)  # 初始化加速度矢量 acceleration vector

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20   # gives upward speed

    def update(self):
        self.acc = vec(0, P_GRA)  # acceleration，x = 0, y = 0.5
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:  # move left
            self.acc.x = -P_ACC
        elif keys[pg.K_d]:  # move right
            self.acc.x = P_ACC
        if abs(self.vel.x) >= 1e-2 or abs(self.acc.x) >= 1e-2:
           self.acc.x += self.vel.x * P_FRI  # add friction in x direction
        else:
           self.vel.x = 0
           self.acc.x = 0
        #self.acc.x += self.vel.x * P_FRI  # add friction in x direction
        self.vel += self.acc  # v = u + at
        self.pos += self.vel + 0.5 * self.acc  # s = ut + 1/2 vt^2

        self.rect.midbottom = self.pos  # for the collision

