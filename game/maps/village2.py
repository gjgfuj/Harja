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
  ["t","g","g","g","g","g","g","g","g","g","g","r","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","g","g","g","g","g","g","g","g","g","g","g","r","g","g","g","g","g","g","t"],
  ["t","t","t","t","t","t","t","t","t","t","t","t","r","t","t","t","t","t","t","t"]
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
  {"type": "level", "position": (12, 19), "level": "village1", "newposition": (12, 1)},
]
scripts = [
]