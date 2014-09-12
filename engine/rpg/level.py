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
    try:
      self.musicname = self.mapfile.music
    except AttributeError:
      self.musicname = None
    try:
      self.mapname = self.mapfile.mapname
    except AttributeError:
      self.mapname = ""
    self.topleft = (600/2-len(self.mapfile.m[0])*30/2, 600/2-len(self.mapfile.m)*30/2)
    self.bindings = {}
    for key in self.mapfile.bindings:
      try:
        self.bindings[key] = pygame.image.load(os.path.join("assets", "tiles", self.mapfile.bindings[key]))
      except pygame.error:
        pass
    self.mapmods = {}
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
    if self.musicname == None:
      pygame.mixer.music.stop()
      gamegeneral.song = None
    if self.musicname != None and gamegeneral.song != self.musicname:
      pygame.mixer.music.load("assets/music/"+self.musicname)
      pygame.mixer.music.play(-1)
      gamegeneral.song = self.musicname
  def save(self):
    eventsave = []
    for event in self.events:
      eventsave.append(event.save())
    return {"eventsave": eventsave, "player": self.player.save(), "mapmods": self.mapmods}
  def load(self, save):
    i = 0
    for eventsave in save["eventsave"]:
      self.events[i].load(eventsave)
      i += 1
    self.player.load(save["player"])
    self.mapmods = save["mapmods"]
    for mod in self.mapmods:
      self.mapfile.m[mod[1]][mod[0]] = self.mapmods[mod]
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
    for event in self.events:
      if event.visible:
        gamegeneral.display.blit(event.sprite, (self.topleft[0]+event.position[0]*30, self.topleft[1]+event.position[1]*30))
    gamegeneral.display.blit(self.player.sprite, (self.topleft[0]+self.player.position[0]*30, self.topleft[1]+self.player.position[1]*30))
    rendered = self.font.render(self.mapname, False, self.mapnamecolor)
    gamegeneral.display.fill((255-self.mapnamecolor[0], 255-self.mapnamecolor[1], 255-self.mapnamecolor[2]), (300-rendered.get_width()/2,3,rendered.get_width(),rendered.get_height()))
    gamegeneral.display.blit(rendered, (300-rendered.get_width()/2,3))
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
    self.mapnamecolor = (200, 0, 20)
class RPGUnderworldLevel(RPGLevel):
  def __init__(self, mapfile):
    RPGLevel.__init__(self, mapfile)
    self.background.fill((0,0,0))
    self.mapnamecolor = (255,255,255)
