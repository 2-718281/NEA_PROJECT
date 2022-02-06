import pygame


class Menu:
    OPTS = ['LEVEL 1', 'LEVEL 2', 'LEVEL 3', 'QUIT']

    def __init__(self, screen):
        self.screen = screen
        self.current = 0

    def run(self, elapse):
        self.draw()
        for e in pygame.event.get():
            if e.type == QUIT:
                return 'quit'
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    self.current = (self.current - 1) % len(self.OPTS)
                elif e.key == K_DOWN:
                    self.current = (self.current + 1) % len(self.OPTS)
                elif e.key == K_RETURN:
                    return self.OPTS[self.current].lower()
        return 'menu'


f = Menu()
