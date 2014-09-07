m = [
  ["#","#","#","#","#"],
  ["#"," "," "," ","#"],
  ["#"," "," "," ","#"],
  ["#"," "," "," ","#"],
  ["#","#"," ","#","#"],
]
bindings = {
  "#": "brickwall.png",
  " ": "brickfloor.png"
}
movement = {
  "#": False,
  " ": True
}
events = [
  {"type": "player", "position": (2,3), "sprite": "player.png"},
  {"type": "level", "position": (2,4), "level": "village1", "newposition": (16, 14)},
]
scripts = [
]
