import pygame as pg

import os
from content.Tools import constant as c

g_F = os.path.dirname(__file__)


class Game:
    def __init__(self):
        pg.init()  # 初始化pygame
        pg.mixer.init()  # 初始化pygame音频
        self.clock = pg.time.Clock()  # 初始化时钟

        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))  # screen
        # this is a layer that move with the camera

        self.background = pg.image.load(os.path.join(i_F, "background.png"))
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, (
            int(self.background_rect.width / 1.33), int(self.background_rect.height / 1.33)))
        self.game_camera = pg.display.set_mode((c.WIDTH, c.HEIGHT)).get_rect()  # camera
        self.game_ground = pg.Surface((self.background_rect.width, self.background_rect.height))
        pg.display.set_caption(c.TITLE)  # init title
        self.font_name = pg.font.match_font(c.FONT_NAME)

        # game running condition
        self.running = True

    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()  # 加载所有sprites
        self.platforms = pg.sprite.Group()
        self.player = Player(self)  # 添加玩家对象
        self.all_sprites.add(self.player)  # 添加玩家对象到sprites
        self.offset_x = 0

        for i, plats in enumerate(c.PLATFORM_LIST):
            p = Platform(*plats, i)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):  # 运行游戏
        self.playing = True
        while not self.player:
            self.clock.tick(c.FPS)  # frame
            self.events()  # check events
            self.update()  # update data
            self.draw(self.screen)  # render the game

    def update(self):

        if self.player.vel.y > 0:  # check hit only when falling
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)  # 检查碰撞 check collision
            if hits:
                self.player.pos.y = hits[0].rect.top + 1  # 停止移动
                self.player.vel.y = 0

        if self.player.rect.right >= c.WIDTH / 4 * 3:
            self.offset_x -= abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x = c.PLATFORM_LIST[plat.index][0] + self.offset_x
                # plat.rect.x -= abs(self.player.vel.x)
                # if plat.rect.right <= 0:
                #    plat.kill()   # kill platforms that are outside the camera
            self.player.pos.x -= abs(self.player.vel.x)  # move player pos leftward so the camera moves rightward

        if self.player.rect.left <= c.WIDTH / 4:
            self.offset_x += abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x = c.PLATFORM_LIST[plat.index][0] + self.offset_x  # abs(self.player.vel.x)
                # if plat.rect.left >= WIDTH:
                #    plat.kill()
            self.player.pos.x += abs(self.player.vel.x)
        self.all_sprites.update()  # 更新sprites

    def events(self):
        for event in pg.event.get():  # 检查事件
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def camera(self):
        bound = self.game_camera.x + self.game_camera.width / 3
        if self.player.vel.x > 0 and self.player.rect.centex > bound:
            self.game_camera.x += self.player.vel.x

    def draw(self, surface):
        self.game_ground.blit(self.background, self.game_camera, self.game_camera)
        self.all_sprites.draw(self.game_ground)
        surface.blit(self.game_ground, (0, 0), self.game_camera)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        self.draw_text("player x pos", 22, WHITE, WIDTH / 4, 0)
        self.draw_text(str(self.player.pos.x), 22, WHITE, WIDTH / 4, 22)

        pg.display.flip()

    def show_start_screen(self):
        # show start screen
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 50, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("press any key to start", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # show go screen when game end/ player die
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.draw_text("game over", 50, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text('your score is' + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4 - 40)
        self.draw_text("press any key to restart", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()

    def wait_for_key(self):
        # wait for player to response
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


game = Game()
game.show_start_screen()  # 显示开始界面
while game.running:  # 运行游戏
    game.new()  # 创建新游戏
    game.show_go_screen()  # 结算游戏

pg.quit()
