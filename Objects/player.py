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
        # jump when not in falling state
        if self.state != s.fall or s.jump:
            self.rect.x += 1
            hits = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 1
            self.vel.y = -20

    def fall(self):
        # terminate state when collide
        pass

    def stand(self):
        # stand
        pass

    def attack(self):
        # attack
        pass

    def damaged(self):
        # if damage, HP-1
        pass

    def move(self):
        # vel change
        pass

    def dead(self):
        # if dead, print game end menu
        pass


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

    # state operations
    def state_change(self, new_state):
        self.state = new_state

    def state_check(self):
        # TODO: change priority
        if self.state == s.jump:
            self.jump()
        elif self.state == s.stand:
            self.stand()
        elif self.state == s.fall:
            self.fall()
        elif self.state == s.attack:
            self.attack()
        elif self.state == s.damaged:
            self.damaged()
        elif self.state == s.dead:
            self.dead()
        elif self.state == s.move:
            self.move()

    @staticmethod
    def collide(obj_1, obj_2):
        collide_stat = pg.spritecollide(obj_1, obj_2)
        return collide_stat
