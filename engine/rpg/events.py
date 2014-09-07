import pygame
import os
from engine import *
from engine.rpg import *

class Event:
  def __init__(self, eventdesc, level):
    self.eventdesc = eventdesc
    self.level = level
    try:
      self.sprite = pygame.image.load(os.path.join("assets", "sprites", eventdesc["sprite"])).convert()
      self.sprite.set_colorkey((0,0,0))
    except KeyError:
      print "Error loading sprite."
      self.sprite = pygame.Surface((30,30))
      self.sprite.set_colorkey((0,0,0))
    except pygame.error:
      print "Error loading sprite."
      self.sprite = pygame.Surface((30,30))
      self.sprite.set_colorkey((0,0,0))
    try:
      self.position = eventdesc["position"]
    except KeyError:
      print "Error at position."
      self.position = (0,0)
    try:
      self.interactive = eventdesc["interactive"]
    except KeyError:
      self.interactive = False
    try:
      self.takescreenshot = eventdesc["screenshot"]
    except KeyError:
      self.takescreenshot = False
  def changelevel(self, level):
    if self.takescreenshot:
      level.background = gamegeneral.display.copy()
    gamegeneral.level = level
  def interact(self):
    pass
  def logic(self):
    pass
class BlockEvent(Event):
  def __init__(self, eventdesc, level):
    Event.__init__(self, eventdesc, level)
    try:
      self.endposition = eventdesc["finalposition"]
    except KeyError:
      print "Error at position"
      self.endposition = (-1, -1)
    try:
      endlevel = eventdesc["level"]
    except KeyError:
      print "Error at level determination."
      self.endlevel = self.level
    try:
      self.endlevel = gamegeneral.levels[endlevel]
    except KeyError:
      print "Error at level fetching from list."
      self.endlevel = self.level
  def interact(self):
    direction = (self.level.player.position[0]-self.level.player.oldposition[0], self.level.player.position[1]-self.level.player.oldposition[1])
    nuposition = (self.position[0]+direction[0], self.position[1]+direction[1])
    if self.position != self.endposition and (self.endposition == nuposition or self.level.mapfile.movement[self.level.mapfile.m[nuposition[1]][nuposition[0]]]):
      self.position = nuposition
    else:
      self.level.player.position = (self.level.player.position[0]-direction[0], self.level.player.position[1]-direction[1])
      return
    if self.position == self.endposition:
      print "Reached end position."
class PlayerEvent(Event):
  def __init__(self, eventdesc, level):
    Event.__init__(self, eventdesc, level)
    self.oldposition = self.position
class LevelEvent(Event):
  def __init__(self, eventdesc, level):
    Event.__init__(self, eventdesc, level)
    try:
      self.nulevel = gamegeneral.levels[eventdesc["level"]]
    except KeyError:
      self.nulevel = self.level
  def interact(self):
    gamegeneral.level = self.nulevel
