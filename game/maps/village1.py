m = [
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","g"],
  ["g","g","r","r","r","r","r","r","r","r","r","r","r","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","r","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","r","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","r","r","r","r","r","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","g","g","g","g","r","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","g","g","g","g","r","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","g","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","g","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","g","g","g","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","r","r","r","r","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g"],
  ["g","g","r","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g"]
]
bindings = {
  "g": "grass.png",
  "r": "road.png"
}
movement = {
  "g": True,
  "r": True,
  " ": False
}
events = [
  {"type": "player", "position": (1, 9), "sprite": "player.png"},
  {"type": "level", "position": (2, 9), "sprite": "archer.png", "level": "archer1", "interactive": True},
  {"type": "block", "position": (4, 5), "sprite": "rock.png", "finalposition": (3, 9), "level": "rocksimple"},
  {"type": "block", "position": (16, 4), "sprite": "rock.png", "finalposition": (5, 9), "level": "rocksimple"},
]
scripts = [
  "intro",
  "archer1",
  "rocksimple"
]
