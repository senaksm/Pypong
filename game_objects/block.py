
import consts
import pyxel


class Block:
    def __init__(self):
        self.x = consts.SCREEN_WIDTH_HALF
        self.y = consts.SCREEN_HEIGHT_HALF - consts.BIG_MARGIN

    def draw(self):
        ''' Draws a block line'''
        pyxel.rectb(self.x, self.y, 1, consts.BIG_MARGIN * 2, consts.WHITE)
