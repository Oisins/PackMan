# -*- coding: utf-8 -*-
from pygame import *




class BordReader:
    def __init__(self):
        self.bordFile = "bord.txt"

    def _readFile(self):
        with open(self.bordFile, "r") as file:
            cont = file.read()
        cont.split("")


class Assets:
    def __init__(self):
        self.assetImg = "assest/assets.png"

    def getAssetByName(self, name):
        return