
import consts
import pyxel

from utils import Point


class Block:
    def __init__(self, center_x, center_y, length_y):
        self.x = center_x
        self.y = center_y - int(length_y / 2)
        self.length_y = length_y
        self.thickness = 1
        # Corner points as x,y cordinates
        self.corners = [Point(self.x, self.y), Point(self.x-self.thickness, self.y+self.length_y)]

    def draw(self):
        ''' Draws a block line'''
        pyxel.rectb(self.x, self.y, self.thickness, self.length_y, consts.RED)
