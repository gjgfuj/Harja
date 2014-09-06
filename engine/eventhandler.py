import engine
class EventHandler:
  def handleevent(self, name):
    if engine.gamegeneral.game.handleevent(name):
      return True
    elif engine.gamegeneral.level.handleevent(name):
      return True
    elif name == "quit":
      engine.gamegeneral.game.quit()
    return False
