m = [
  ["t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","t"],
  ["t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t","t"]
]
bindings = {
  "g": "grass.png",
  "t": "tree.png",
  "r": "road.png"
}
movement = {
  "g": True,
  "t": False,
  "r": True
}
events = [
  {"type": "player", "sprite": "player.png"},
  {"type": "level", "position": (0, 15), "level": "forest1", "newposition": (18, 15)},
  {"type": "level", "position": (1, 16), "level": "hiddenvillage.lever", "screenshot": True, "interactive": True, "sprite": "leverhole.png"}
]
scripts = [
  "hiddenvillage.lever"
]
