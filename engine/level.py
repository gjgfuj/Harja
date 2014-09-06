import pygame
import engine
class Level:
  def __init__(self):
    self.background = pygame.Surface((engine.gamegeneral.resolution))
    self.background.fill((0,0,0))
    self.levelvars = {}
    self.font = engine.gamegeneral.font
  def logic(self):
    pass
  def render(self):
    engine.gamegeneral.display.blit(self.background, (0,0))
  def handleevent(self, event):
    return False
