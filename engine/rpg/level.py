import pygame
import os
from engine import *
from engine.rpg import *
class RPGLevel(Level):
  def __init__(self, mapfile):
    Level.__init__(self)
    self.mapfile = mapfile
    self.bindings = {}
    for key in self.mapfile.bindings:
      self.bindings[key] = pygame.image.load(os.path.join("assets", "tiles", self.mapfile.bindings[key]))
    self.events = []
    for event in self.mapfile.events:
      if event["type"] == "player":
        self.player = PlayerEvent(event, self)
      elif event["type"] == "level":
        self.events.append(LevelEvent(event, self))
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
          gamegeneral.display.blit(self.bindings[ay], (x*30, y*30))
        except KeyError:
          pass
        x += 1
      x = 0
      y += 1
    gamegeneral.display.blit(self.player.sprite, (self.player.position[0]*30, self.player.position[1]*30))
    for event in self.events:
      gamegeneral.display.blit(event.sprite, (event.position[0]*30, event.position[1]*30))
  def handleevent(self, event):
    if Level.handleevent(self, event):
      return True
    if event == "interact":
      for event in self.events:
        if event.position == self.player.position:
          event.interact()	
    elif event == "up":
      if self.player.position[1] != 0:
        if self.mapfile.movement[self.mapfile.m[self.player.position[0]][self.player.position[1]-1]]:
          self.player.position = (self.player.position[0], self.player.position[1]-1)
    elif event == "down":
      try:
        if self.mapfile.movement[self.mapfile.m[self.player.position[0]][self.player.position[1]+1]]:
          self.player.position = (self.player.position[0], self.player.position[1]+1)
      except IndexError:
        pass
    elif event == "left":
      if self.player.position[0] != 0:
        if self.mapfile.movement[self.mapfile.m[self.player.position[0]-1][self.player.position[1]]]:
          self.player.position = (self.player.position[0]-1, self.player.position[1])
    elif event == "right":
      try:
        if self.mapfile.movement[self.mapfile.m[self.player.position[0]+1][self.player.position[1]]]:
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
    self.background.fill((200,70,40))
