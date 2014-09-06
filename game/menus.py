from engine import *
import pygame

class PrimaryMenu(Menu):
  def __init__(self):
    Menu.__init__(self, [("Options", self.options, None), ("Back", self.prevmenu, None)], (500, 300), True)
    self.optionsmenu = OptionsMenu()
  def options(self, a):
    self.optionsmenu.entermenu(self.oldlevel)
class OptionsMenu(Menu):
  def __init__(self):
    Menu.__init__(self, [("Fullscreen", self.fullscreen, None), ("Back", self.prevmenu, None)], (500, 300), True)
    self.fullscreen = False
  def fullscreen(self, a):
    if self.fullscreen:
      gamegeneral.display = pygame.display.set_mode(gamegeneral.resolution)
    else:
      gamegeneral.display = pygame.display.set_mode(gamegeneral.resolution, pygame.FULLSCREEN)
