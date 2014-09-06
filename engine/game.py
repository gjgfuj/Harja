import pygame
import engine
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
