import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from objecct_renderer import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill("black")
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


            _ = False
            if PLAYER_POS == 3:
                mini_map = [
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
                    [2, _, _, 1, 1, 1, 4, _, _, _, 2, 2, 2, _, _, 2],
                    [2, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 2],
                    [1, 1, 1, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
                    [1, _, _, 3, 1, 1, 4, _, _, 1, 1, 1, 1, 1, _, 1],
                    [1, 1, 1, 1, _, 1, _, _, _, 1, _, 1, _, 1, _, 1],
                    [1, _, _, 1, _, 1, _, _, _, 1, _, 1, _, 1, _, 1],
                    [1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 1],
                ]

if __name__ == '__main__':
    game = Game()
    game.run()

