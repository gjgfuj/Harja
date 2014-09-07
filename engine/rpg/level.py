import pygame
import os
import importlib
from engine import *
import engine.vnovel as vnovel
from engine.rpg import *
class RPGLevel(Level):
  def __init__(self, mapfile):
    Level.__init__(self)
    self.mapfile = mapfile
    try:
      for script in self.mapfile.scripts:
        s = importlib.import_module("game.scripts."+script)
        gamegeneral.levels[script] = vnovel.VNovelLevel(s)
        print "Imported "+script
    except AttributeError:
      print "No scripts."
    self.topleft = (600/2-len(self.mapfile.m[0])*30/2, 600/2-len(self.mapfile.m)*30/2)
    self.bindings = {}
    for key in self.mapfile.bindings:
      try:
        self.bindings[key] = pygame.image.load(os.path.join("assets", "tiles", self.mapfile.bindings[key]))
      except pygame.error:
        pass
  def init(self):
    self.events = []
    for event in self.mapfile.events:
      if event["type"] == "player":
        self.player = PlayerEvent(event, self)
      elif event["type"] == "level":
        self.events.append(LevelEvent(event, self))
      elif event["type"] == "block":
        self.events.append(BlockEvent(event, self))
  def logic(self):
    for event in self.events:
      if (not event.interactive) and event.position == self.player.position:
        event.interact()
      event.logic()
  def render(self):
    Level.render(self)
    x = 0
    y = 0
    for ax in self.mapfile.m:
      for ay in ax:
        try:
          gamegeneral.display.blit(self.bindings[ay], (self.topleft[0]+x*30, self.topleft[1]+y*30))
        except KeyError:
          pass
        x += 1
      x = 0
      y += 1
    gamegeneral.display.blit(self.player.sprite, (self.topleft[0]+self.player.position[0]*30, self.topleft[1]+self.player.position[1]*30))
    for event in self.events:
      gamegeneral.display.blit(event.sprite, (self.topleft[0]+event.position[0]*30, self.topleft[1]+event.position[1]*30))
  def handleevent(self, event):
    if Level.handleevent(self, event):
      return True
    if event == "interact":
      for event in self.events:
        if event.position == self.player.position:
          event.interact()	
    elif event == "up":
      if self.player.position[1] != 0:
        if self.mapfile.movement[self.mapfile.m[self.player.position[1]-1][self.player.position[0]]]:
          self.player.oldposition = self.player.position
          self.player.position = (self.player.position[0], self.player.position[1]-1)
    elif event == "down":
      try:
        if self.mapfile.movement[self.mapfile.m[self.player.position[1]+1][self.player.position[0]]]:
          self.player.oldposition = self.player.position
          self.player.position = (self.player.position[0], self.player.position[1]+1)
      except IndexError:
        pass
    elif event == "left":
      if self.player.position[0] != 0:
        if self.mapfile.movement[self.mapfile.m[self.player.position[1]][self.player.position[0]-1]]:
          self.player.oldposition = self.player.position
          self.player.position = (self.player.position[0]-1, self.player.position[1])
    elif event == "right":
      try:
        if self.mapfile.movement[self.mapfile.m[self.player.position[1]][self.player.position[0]+1]]:
          self.player.oldposition = self.player.position
          self.player.position = (self.player.position[0]+1, self.player.position[1])
      except IndexError:
        pass
class RPGOverworldLevel(RPGLevel):
  def __init__(self, mapfile):
    RPGLevel.__init__(self, mapfile)
    self.background.fill((0,200,0))
class RPGUnderworldLevel(RPGLevel):
  def __init__(self, mapfile):
    RPGLevel.__init__(self, mapfile)
    self.background.fill((0,0,0))
