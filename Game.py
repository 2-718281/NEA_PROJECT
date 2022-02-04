# this is the main game class
class Game:

    def __init__(self):


    def new_game(self):
        for i, plats in enumerate(c.PLATFORM_LIST):
            p = Platform(*plats, i)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def read_game(self):
        pass
