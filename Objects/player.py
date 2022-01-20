from Tools import constant as c, paths, states as s
import pygame as pg

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):  # inherit from sprite

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)  # init sprite
        self.game = game
        self.image = pg.Surface((50, 50)).fill(c.GREEN)

        self.rect = self.image.get_rect()  # get rect
        self.rect.center = (c.WIDTH / 2, c.HEIGHT / 2)
        
        self.pos = vec(c.WIDTH / 2, c.HEIGHT / 2)  # position vector
        self.vel = vec(0, 0)  # velocity vector
        self.acc = vec(0, 0)  # acceleration vector
        self.HP = c.P_HP
        self.state = s.start

    def jump(self):
        if self.state != s.fall:
            self.rect.x += 1
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 1
            if hits:
                self.vel.y = -20  # gives upward speed
            self.state = s.fall

    def fall(self):
        hits =
        self.state = s.stand


    def state_check(self):
        if self.state == s.jump:
            self.jump()


    def update(self):
        self.acc = vec(0, c.P_GRA)  # acceleration，x = 0, y = 0.5
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:  # move left
            self.acc.x = -c.P_ACC
        elif keys[pg.K_d]:  # move right
            self.acc.x = c.P_ACC

        if abs(self.vel.x) >= 1e-2 or abs(self.acc.x) >= 1e-2:
            self.acc.x += self.vel.x * c.P_FRI  # add friction in x direction

        else:
            self.vel.x = 0
            self.acc.x = 0

        # self.acc.x += self.vel.x * P_FRI  # add friction in x direction
        self.vel += self.acc  # v = u + at
        self.pos += self.vel + 0.5 * self.acc  # s = ut + 1/2 vt^2

        self.rect.midbottom = self.pos  # for the collision
