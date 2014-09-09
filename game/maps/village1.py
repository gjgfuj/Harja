m = [
  ["t","t","t","t","t","t","t","t","t","t","t","t","r","t","t","t","t","t","t","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","r","r","r","r","r","r","r","r","r","r","r","g","g","g","g","g","g","t"],
  ["t","g","r","h","g","h","g","g","r","g","g","r","g","g","g","g","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","r","g","g","g","g","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","r","r","r","r","r","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","g","g","g","g","r","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","g","g","g","g","r","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","g","g","g","g","r","r","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","r","r","r","r","g","g","g","g","g","g","g","t"],
  ["t","g","r","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","t","r","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t"]
]
bindings = {
  "g": "grass.png",
  "r": "road.png",
  "t": "tree.png",
  "h": "rockhole.png",
}
movement = {
  "g": True,
  "r": True,
  "t": False,
  "h": False,
  "#": True
}
events = [
  {"type": "player", "position": (1, 9), "sprite": "player.png"},
  {"type": "level", "position": (16, 13), "level": "village1house1", "newposition": (3,5), "sprite": "house.png"},
  {"type": "level", "position": (10, 16), "level": "village1house2", "newposition": (2,3), "sprite": "house.png"},
  {"type": "level", "position": (12, 0), "level": "village2", "newposition": (12, 18)},
  {"type": "level", "position": (2, 19), "level": "forest1", "newposition": (2, 1)},
  {"type": "level", "position": (2, 9), "sprite": "archer.png", "level": "archer1", "interactive": True, "screenshot": True},
  {"type": "block", "position": (4, 5), "sprite": "rock.png", "finalposition": (3, 9), "level": "rocksimple", "screenshot": True},
  {"type": "block", "position": (16, 4), "sprite": "rock.png", "finalposition": (5, 9), "level": "rocksimple", "screenshot": True},
]
scripts = [
  "intro",
  "archer1",
  "rocksimple"
]
