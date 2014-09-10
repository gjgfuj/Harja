from engine import *
import pygame

class PrimaryMenu(Menu):
  def __init__(self):
    Menu.__init__(self, [("Stats", self.stats, None), ("Options", self.options, None), ("Save", self.save, None), ("Load", self.load, None), ("Back", self.prevmenu, None)], (400, 300), True)
    self.optionsmenu = OptionsMenu()
    self.statsmenu = StatsMenu()
  def options(self, a):
    self.optionsmenu.entermenu(self)
  def stats(self, a):
    self.statsmenu.entermenu(self)
class StatsMenu(Menu):
  def __init__(self):
    Menu.__init__(self, [("Back", self.prevmenu, None)], (500, 500), True)
  def render(self):
    Menu.render(self)
    gamegeneral.display.blit(self.font.render("Karma: "+str(gamegeneral.game.globalvars["karma"]), True, self.boxcolor), (200, 200))
class OptionsMenu(Menu):
  def __init__(self):
    Menu.__init__(self, [("Back", self.prevmenu, None)], (400, 300), True)
    self.fullscreen = False
  def fullscreen(self, a):
    if self.fullscreen:
      gamegeneral.display = pygame.display.set_mode(gamegeneral.resolution)
    else:
      gamegeneral.display = pygame.display.set_mode(gamegeneral.resolution, pygame.FULLSCREEN)
