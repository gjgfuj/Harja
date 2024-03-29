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
  {"type": "level", "position": (2,4), "level": "village1", "newposition": (10, 17)},
  {"type": "level", "position": (2,2), "level": "village1.nameless2", "screenshot": True, "interactive": True, "sprite": "villager.png"}
]
scripts = [
  "village1.nameless2"
]
mapname = "Marki Village House"
music = "Village.ogg"
