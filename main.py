import pygame
pygame.init()
import engine
import game.general
import game.keys
game.general.display = pygame.display.set_mode(game.general.resolution)
engine.gamegeneral = game.general
game.general.engine = engine
game.general.game = engine.Game()
game.general.eventhandler = engine.EventHandler()
game.general.level = engine.Level()
def main():
  import game.main
  for level in game.general.levels:
    game.general.levels[level].init()
  while game.general.isRunning:
    for event in pygame.event.get():
      try:
        if event.type == pygame.QUIT:
          game.general.game.quit()
        elif event.type == pygame.KEYDOWN:
          game.general.eventhandler.handleevent(game.keys.keydown[event.key])
        elif event.type == pygame.KEYUP:
          game.general.eventhandler.handleevent(game.keys.keyup[event.key])
        elif event.type == pygame.MOUSEBUTTONUP:
          game.general.eventhandler.handleevent(game.keys.mouseup[event.button])
        elif event.type == pygame.MOUSEBUTTONDOWN:
          game.general.eventhandler.handleevent(game.keys.mousedown[event.button])
      except KeyError:
        pass
    game.general.level.logic()
    game.general.game.logic()
    game.general.display.fill((0,0,0))
    game.general.level.render()
    game.general.game.render()
    pygame.display.flip()
if __name__ == "__main__":
  main()
