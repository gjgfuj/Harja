import pygame
import engine
import importlib
class Game:
  def __init__(self):
    self.globalvars = {}
    self.font = engine.gamegeneral.font
  def quit(self):
    engine.gamegeneral.isRunning = False
  def logic(self):
    pass
  def render(self):
    pass
  def handleevent(self, event):
    return False
  def importmap(self, mapname, leveltype):
    m = importlib.import_module("game.maps."+mapname)
    engine.gamegeneral.levels[mapname] = leveltype(m)
    print "Imported "+mapname
