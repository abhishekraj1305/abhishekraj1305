from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        pass


class engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(scene):

    def enter(self):
        pass

class centralcorridor(scene):

    def enter(self):
        pass

class LaserWeaponArmory(scene):

    def enter(self):
        pass

class Thebridge(scene):

    def enter(self):
        pass

class escapepod(scene):

    def enter(self):
        pass 


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = engine(a_map)
a_game.play()     






