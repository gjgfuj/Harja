import pygame
import engine
import sys
import os
import importlib
class Menu(engine.Level):
  def __init__(self, options, coords, vertical=True, color=(100, 100, 100)):
    engine.Level.__init__(self)
    self.options = {}
    self.color = color
    self.boxcolor = (0,0,255)
    self.oldlevel = self
    x = coords[0]
    nux = 0
    y = coords[1]
    nuy = 0
    self.boxrect = (x, y, 0, 0)
    for option in options:
      self.options[(x, y, self.font.render(option[0], False, color).get_width()+10, 30)] = option
      if vertical:
        y += 30
        nuy += 30
        if self.font.render(option[0], False, color).get_width()+10 > nux:
          nux = self.font.render(option[0], False, color).get_width()+10
        self.boxrect = (self.boxrect[0], self.boxrect[1], nux, nuy)
      else:
        x += self.font.render(option, False, color).get_width()+10
  def entermenu(self, level):
    engine.gamegeneral.level = self
    if self != level:
      self.oldlevel = level
    engine.gamegeneral.game.inmenu = True
    engine.gamegeneral.sounds["TextContinue.ogg"].play()
  def quit(self, a):
    engine.gamegeneral.game.quit()
  def prevmenu(self, a):
    engine.gamegeneral.level = self.oldlevel
    engine.gamegeneral.game.inmenu = False
  def save(self, a):
    self.prevmenu(a)
    f = open("save.py", "w")
    f.write("globalvars = "+repr(engine.gamegeneral.game.globalvars)+"\n")
    levelsaves = {}
    for level in engine.gamegeneral.levels:
      if engine.gamegeneral.levels[level] == engine.gamegeneral.level:
        f.write("currentlevel = "+repr(level)+"\n")
      levelsaves[level] = engine.gamegeneral.levels[level].save()
    f.write("levelsaves = "+repr(levelsaves))
    f.close()
  def load(self, a):
    f = open("save.py", "rb")
    exec f
    f.close()
    engine.gamegeneral.game.globalvars = globalvars
    engine.gamegeneral.level = engine.gamegeneral.levels[currentlevel]
    for levelsave in levelsaves:
      engine.gamegeneral.levels[levelsave].load(levelsaves[levelsave])
    engine.gamegeneral.game.inmenu = False
  def render(self):
    engine.Level.render(self)
    engine.gamegeneral.display.fill(self.boxcolor, self.boxrect)
    for option in self.options:
      engine.gamegeneral.display.blit(self.font.render(self.options[option][0], False, self.color), option)
  def handleevent(self, event):
    engine.Level.handleevent(self, event)
    if event == "click":
      pos = pygame.mouse.get_pos()
      for option in self.options:
        if option[0] < pos[0] < option[0]+option[2]:
          if option[1] < pos[1] < option[1]+option[3]:
            self.options[option][1](self.options[option][2])
            engine.gamegeneral.sounds["TextContinue.ogg"].play()
