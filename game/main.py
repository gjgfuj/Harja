import pygame

import engine
import engine.vnovel as vnovel
import engine.rpg as rpg

from game.menus import *

class HarjaGame(engine.Game):
  def __init__(self):
    engine.Game.__init__(self)
    self.importmap("village1", rpg.RPGOverworldLevel)
    self.importmap("village1house1", rpg.RPGUnderworldLevel)
    self.importmap("village1house2", rpg.RPGUnderworldLevel)
    self.importmap("village2", rpg.RPGOverworldLevel)
    self.importmap("forest1", rpg.RPGOverworldLevel)
    self.importmap("hiddenvillage", rpg.RPGOverworldLevel)
    self.importmap("forestdungeon.entry", rpg.RPGUnderworldLevel)
    engine.gamegeneral.level = engine.gamegeneral.levels["intro"]
    self.menu = PrimaryMenu()
    self.inmenu = False
  def handleevent(self, event):
    if event == "click":
      if not self.inmenu:
        pos = pygame.mouse.get_pos()
        if engine.gamegeneral.display.get_width()-50 < pos[0] < engine.gamegeneral.display.get_width():
          if engine.gamegeneral.display.get_height()-25 < pos[1] < engine.gamegeneral.display.get_height():
            self.menu.entermenu(engine.gamegeneral.level)
            return True
  def render(self):
    if not self.inmenu:
      engine.gamegeneral.display.fill((234, 123, 141), (engine.gamegeneral.display.get_width()-50, engine.gamegeneral.display.get_height()-25, 50, 25))
      engine.gamegeneral.display.blit(self.font.render("Menu", False, (255,255,255)), (engine.gamegeneral.display.get_width()-45, engine.gamegeneral.display.get_height()-20))
engine.gamegeneral.game = HarjaGame()
