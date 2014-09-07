from engine import *
import os
import pygame
class VNovelMenu(menu.Menu):
  def __init__(self, level, options, color):
    self.level = level
    nuoptions = []
    for o in options:
      nuoptions.append((o, self.setflag, o))
    menu.Menu.__init__(self, nuoptions, (150, 150), True, color)
  def setflag(self, flag):
    print flag
    self.level.levelvars["menu"] = flag
    self.prevmenu(flag)
class VNovelLevel(level.Level):
  def __init__(self, script):
    Level.__init__(self)
    self.script = script.script
    self.color = (255,255,255)
    self.boxcolor = (155, 110, 40)
    self.speakercolor = (255,255,255)
    self.index = 0
    self.indexchanged = True
    self.font = gamegeneral.font
    self.speaker = ""
  def actionperform(self):
    self.indexchanged = False
    try:
      scriptpiece = self.script[self.index]
      for actiondef in scriptpiece["actions"]:
        action = actiondef["action"]
        if action == "changelevel":
          engine.gamegeneral.level = engine.gamegeneral.levels[actiondef["level"]]
          try:
            if actiondef["resetindex"]:
              self.index = -1
              self.indexchanged = True
          except KeyError:
            pass
        elif action == "setindex":
          self.index = actiondef["index"]
          self.indexchanged = True
        elif action == "color":
          self.color = actiondef["color"]
        elif action == "speakercolor":
          self.speakercolor = actiondef["color"]
        elif action == "font":
          if actiondef["type"] == "system":
            self.font = pygame.font.SysFont(actiondef["font"], 20)
          else:
            self.font = pygame.font.Font(actiondef["font"], 20)
        elif action == "bgfile":
          self.background = pygame.image.load(os.path.join("assets", "bg", actiondef["filename"]))
        elif action == "bgcolor":
          self.background.fill(actiondef["color"])
        elif action == "boxcolor":
          self.boxcolor = actiondef["color"]
        elif action == "bgsurface":
          self.background = actiondef["surface"]
        elif action == "menu":
          menu = VNovelMenu(self, actiondef["options"], self.color)
          menu.background = self.background
          menu.boxcolor = self.boxcolor
          menu.entermenu(self)
          #self.index += 1
        elif action == "changetile":
          try:
            level = gamegeneral.levels[actiondef["level"]]
            level.mapfile.m[actiondef["position"][1]][actiondef["position"][0]] = actiondef["tile"]
          except KeyError:
            print "changetile KeyError"
          except IndexError:
            print "changetile IndexError"
        elif action == "set":
          try:
            actiondef["global"]
            g = True
          except KeyError:
            g = False
          try:
            key = actiondef["key"]
          except KeyError:
            key = "flag"
          try:
            value = actiondef["value"]
          except KeyError:
            value = True
          if g:
            gamegeneral.game.globalvars[key] = value
          else:
            self.levelvars[key] = value
        elif action == "add":
          try:
            actiondef["global"]
            g = True
          except KeyError:
            g = False
          try:
            key = actiondef["key"]
          except KeyError:
            key = "flag"
          try:
            value = actiondef["value"]
          except KeyError:
            value = True
          try:
            if g:
              gamegeneral.game.globalvars[key] += value
            else:
              self.levelvars[key] += value
          except KeyError:
            if g:
              gamegeneral.game.globalvars[key] = value
            else:
              self.levelvars[key] = value
        elif action == "test":
          try:
            actiondef["global"]
            g = True
          except KeyError:
            g = False
          try:
            key = actiondef["key"]
          except KeyError:
            key = "flag"
          try:
            value = actiondef["value"]
          except KeyError:
            value = True
          try:
            test = actiondef["test"]
          except KeyError:
            test = "="
          try:
            if g:
              var = gamegeneral.game.globalvars[key]
            else:
              var = self.levelvars[key]
          except KeyError:
            continue
          if test == "=":
            if var == value:
              self.index = actiondef["index"]
              self.indexchanged = True
          elif test == "<":
            if var < value:
              self.index = actiondef["index"]
              self.indexchanged = True
          if test == ">":
            if var >  value:
              self.index = actiondef["index"]
              self.indexchanged = True
    except IndexError:
      print "Index Error."
    except KeyError:
      pass
    try:
      line = self.script[self.index]["line"]
    except IndexError:
      self.index = 0
      self.indexchanged = True
    except KeyError:
      self.index += 1
      self.indexchanged = True
    try:
      self.speaker = self.script[self.index]["speaker"]
    except IndexError:
      pass
    except KeyError:
      pass
  def logic(self):
    if self.indexchanged:
      self.actionperform()
  def render(self):
    Level.render(self)
    y = 375
    gamegeneral.display.fill(self.boxcolor, (20, 375, 560, 100))
    try:
      gamegeneral.display.blit(self.font.render(self.speaker, True, self.speakercolor), (20, y))
    except KeyError:
      pass
    y += 25
    try:
      gamegeneral.display.blit(self.font.render(self.script[self.index]["line"], True, self.color), (40, y))
    except IndexError:
      pass
    except KeyError:
      pass
  def handleevent(self, event):
    if Level.handleevent(self, event):
      return True
    if event == "interact" or event == "click":
      self.index += 1
      self.indexchanged = True
      return True

