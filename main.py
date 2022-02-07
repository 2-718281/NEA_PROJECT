import pygame as pg
import pygame_menu
import os
import json
from content.Tools import constant as c, states as st , db as db
from content.Objects import player as obj_p
from content.Objects import platform as obj_pl
from content.Map import room


g_F = os.path.dirname(__file__)
i_F = os.path.join(g_F, "res/img")

class Game:
    def __init__(self):
        pg.init()  # 初始化pygame
        pg.mixer.init()  # 初始化pygame音频
        self.clock = pg.time.Clock()  # 初始化时钟

        self.screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))  # screen
        # this is a layer that move with the camera
        '''
        self.background = pg.image.load(os.path.join(i_F, "background.png"))
        '''
        self.background = pg.Surface((c.BACKGROUND_WIDTH,c.BACKGROUND_HEIGHT))
        self.background.fill(c.WHITE)
        self.background_rect = self.background.get_rect()
        '''self.background = pg.transform.scale(self.background, (int(self.background_rect.width / 1.33), int(self.background_rect.height / 1.33)))'''

        self.game_camera = pg.display.set_mode((c.WIDTH, c.HEIGHT)).get_rect()  # camera
        self.game_ground = pg.Surface((self.background_rect.width, self.background_rect.height))
        pg.display.set_caption(c.TITLE)  # init title
        self.font_name = pg.font.match_font(c.FONT_NAME)
        self.user = db.db('USER',{'GUEST':''})
        with open('USER') as json_file:
            self.user_dict = json.load(json_file)

        self.name = 'GUEST'
        self.password = ''
        # game running condition
        self.running = True
        self.start_menu()

    def map_gen(self):
        r = room.Room()
        self.a = r.generate_map()
        self.plat = r.plat_dict_getter()
        self.trap = r.trap_dict_getter()
        self.PLATFORM_LIST =list(self.plat.values())
        self.TRAP_LIST = list(self.trap.values())
        self.SPAWNING_POINT = c.SPAWNING_POINT
        self.END_POINT = c.END_POINT

        print(self.plat)
        with open('PLATFORMS', 'w+') as outfile:
            json.dump(self.plat, outfile)
        with open('TRAPS','w+') as outfile:
            json.dump(self.trap,outfile)

    def update_db(self,name):
        self.user_dict[name] = ''
        self.user.replace_db(self.user_dict)

    def start_menu(self):
        menu = pygame_menu.Menu('Welcome', c.WIDTH, c.HEIGHT,
                               theme=pygame_menu.themes.THEME_BLUE)
        menu.add.text_input('Name :', default='John Doe', onreturn=self.update_db)
        menu.add.button('Play', self.start_the_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def end_menu(self):
        end_menu = pygame_menu.Menu('GAME END', c.WIDTH, c.HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)
        end_menu.mainloop(self.screen)


    def new(self):
        self.map_gen()
        self.score = 0
        self.all_sprites = pg.sprite.Group()  # 加载所有sprites
        self.platforms = pg.sprite.Group()
        self.traps = pg.sprite.Group()
        self.start = pg.sprite.Group()
        self.end = pg.sprite.Group()

        self.player = obj_p.Player(self)  # 添加玩家对象
        self.all_sprites.add(self.player)  # 添加玩家对象到sprites
        self.offset_x = 0
        self.playing = True

        for i, plats in enumerate(self.plat.values()):
            p = obj_pl.Platform(*plats, i)
            self.all_sprites.add(p)
            self.platforms.add(p)

        for i, traps in enumerate(self.trap.values()):
            t = obj_pl.Trap(*traps, i)
            self.all_sprites.add(t)
            self.traps.add(t)

        for i, start in enumerate(self.SPAWNING_POINT):
            s = obj_pl.Starting(*start, i)
            self.all_sprites.add(s)
            self.start.add(s)

        for i, end in enumerate(self.END_POINT):
            e = obj_pl.Ending(*end, i)
            self.all_sprites.add(e)
            self.end.add(e)

        self.render_mini_map(self.a)
        self.run()

    def run(self):  # 运行游戏
        while no self.player.dead st.dead and self.player.state != st.passed:
            self.clock.tick(c.FPS)  # frame
            self.events()  # check events
            self.update()  # update data
            self.draw(self.screen)  # render the game
        self.end_menu()

    def update(self):
        if self.player.vel.y > 0:  # check hit only when falling
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)  # 检查碰撞 check collision
            if hits:
                self.player.pos.y = hits[0].rect.top + 1  # 停止移动
                self.player.vel.y = 0
            hits = pg.sprite.spritecollide(self.player, self.traps,False)
            if hits:
                self.player.HP -= 1
                self.player.state = st.super
                self.player.pos.y = hits[0].rect.top + 1  # 停止移动
                self.player.vel.y = 0
            hits = pg.sprite.spritecollide(self.player, self.start, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1  # 停止移动
                self.player.vel.y = 0
            hits = pg.sprite.spritecollide(self.player, self.end, False)
            if hits:
                self.player.state = st.passed

        if self.player.rect.right >= c.WIDTH / 4 * 3:
            self.offset_x -= abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x = self.PLATFORM_LIST[plat.index][0] + self.offset_x
                # plat.rect.x -= abs(self.player.vel.x)
                # if plat.rect.right <= 0:
                #    plat.kill()   # kill platforms that are outside the camera
            for trap in self.traps:
                trap.rect.x = self.TRAP_LIST[trap.index][0] + self.offset_x

            for s in self.start:
                s.rect.x = self.SPAWNING_POINT[s.index][0] + self.offset_x

            for e in self.end:
                e.rect.x = self.END_POINT[e.index][0] + self.offset_x
            self.player.pos.x -= abs(self.player.vel.x)  # move player pos leftward so the camera moves rightward

        if self.player.rect.left <= c.WIDTH / 4:
            self.offset_x += abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x = self.PLATFORM_LIST[plat.index][0] + self.offset_x  # abs(self.player.vel.x)
            for trap in self.traps:
                trap.rect.x = self.TRAP_LIST[trap.index][0] + self.offset_x

            for s in self.start:
                s.rect.x = self.SPAWNING_POINT[s.index][0] + self.offset_x

            for e in self.end:
                e.rect.x = self.END_POINT[e.index][0] + self.offset_x

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
        self.draw_text(str(self.score), 22, c.WHITE, c.WIDTH / 2, 15)
        self.draw_text("player x pos", 22, c.WHITE, c.WIDTH / 4, 0)
        self.draw_text(str(self.player.pos.x), 22, c.WHITE, c.WIDTH / 4, 22)

        pg.display.flip()

    def show_start_screen(self):
        # show start screen
        self.screen.fill(c.BLACK)
        self.draw_text(c.TITLE, 50, c.WHITE, c.WIDTH / 2, c.HEIGHT / 4)
        self.draw_text("press any key to start", 22, c.WHITE, c.WIDTH / 2, c.HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        # wait for player to response
        waiting = True
        while waiting:
            self.clock.tick(c.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


    def start_the_game(self):
        self.new()

    def render_mini_map(self, map):  # render map background

        for i in range(map.shape[0]):
            print_str = ''
            for j in range(map.shape[1]):
                if map[i, j] == 1:
                    print_str += '#'
                elif map[i, j] == 2:
                    print_str += 'T'
                elif map[i, j] == 3:
                    print_str += ''
                elif map[i, j] == 4:
                    print_str += 'S'
                elif map[i, j] == 5:
                    print_str += 'E'
                else:
                    print_str += " "
            print(print_str)

game = Game()
game.show_start_screen()  # 显示开始界面
while game.running:  # 运行游戏
    game.new()  # 创建新游戏

pg.quit()
