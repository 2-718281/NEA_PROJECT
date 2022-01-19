# test terminal UI
# UI gets items from save json file.

class UI:

    def __init__(self):
        self.clock = 30
        self.playing = True

    def new_frame(self):  # render new frame
        while self.playing:
            self.render_map()
            self.render_player()
            self.render_platform()
            self.render_trap()

    def halt(self):
        if input == 'p':
            self.playing == False

    def render_map(self):  # render map background
        pass

    def render_player(self):
        pass

    def render_platform(self, pos):
        pass

    def render_trap(self):
        pass

    def render_item(self):
        pass

    def render_collision_box(self):
        pass

