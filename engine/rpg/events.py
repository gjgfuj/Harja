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
  def interact(self):
    pass
  def logic(self):
    pass
class PlayerEvent(Event):
  def __init__(self, eventdesc, level):
    Event.__init__(self, eventdesc, level)
class LevelEvent(Event):
  def __init__(self, eventdesc, level):
    Event.__init__(self, eventdesc, level)
    try:
      self.nulevel = gamegeneral.levels[eventdesc["level"]]
    except KeyError:
      self.nulevel = self.level
  def interact(self):
    gamegeneral.level = self.nulevel
