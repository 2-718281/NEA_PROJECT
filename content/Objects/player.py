import pygame as pg
import sys
import random
from content.Tools import constant as c, states as s
import os
import time

pg.init()
vec = pg.math.Vector2

g_F = os.path.dirname(__file__)
i_F = os.path.join(g_F, "img")


class Player(pg.sprite.Sprite):  # inherit from sprite
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)  # 初始化sprite
        self.game = game
        self.image = pg.Surface((50, 50))
        self.image.fill(c.GREEN)
        self.rect = self.image.get_rect()  # 获取正方形 get rect
        self.rect.center = (c.WIDTH/2, c.HEIGHT/2)
        self.pos = vec(c.WIDTH / 2, c.HEIGHT / 2)  # 初始化位置矢量 position vector
        self.vel = vec(0, 0)  # 初始化速度矢量 velocity vector
        self.acc = vec(0, 0)  # 初始化加速度矢量 acceleration vector
        self.HP = 10
        self.state = s.stand

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20   # gives upward speed
        self.state = s.fall

    def update(self):
        self.check_state()
        self.acc = vec(0, c.P_GRA)  # acceleration，x = 0, y = 0.5
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:  # move left
            self.acc.x = -c.P_ACC
        elif keys[pg.K_d]:  # move right
            self.acc.x = c.P_ACC

        self.acc.x += self.vel.x * c.P_FRI  # add friction in x direction
        self.vel += self.acc  # v = u + at
        self.pos += self.vel + 0.5 * self.acc  # s = ut + 1/2 vt^2

        self.rect.midbottom = self.pos  # for the collision

    def check_state(self):
        if self.state == s.super:
            HP = self.HP
            self.HP = 999999999999999
            time.sleep(1)
            self.HP = HP

    def dead(self):
        if self.pos.y >= c.HEIGHT:
            self.state = s.dead
            return True
        elif self.HP == 0:
            self.state = s.dead
            return True
        return False
