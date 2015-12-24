# -*- coding: utf-8 -*-
from pygame import *


class BordReader:
    def __init__(self):
        self.bordFile = "board.txt"
        self.board = []

        class Tile:
            def __init__(self, x, y, wall):
                self.x = x
                self.y = y
                self.wall = wall

            def draw(self):
                pass

    def _readFile(self):
        bord = []
        with open(self.bordFile, "r") as file:
            content = file.read().split("\n")
            return [list(i) for i in content]

    def _decodeBoard(self):
        fileBoard = self._readFile()
        board = []
        for indexX, x in enumerate(fileBoard):
            board.append([])
            for indexY, y in enumerate(x):
                board[indexX].append(Tile(indexX, indexY, y == "#"))
        return board


    def getBoard(self):
        return self._decodeBoard()


class Assets:
    def __init__(self):
        self.assetImg = "assest/assets.png"

    def getAssetByName(self, name):
        return

b = BordReader()
print(b.getBoard())
