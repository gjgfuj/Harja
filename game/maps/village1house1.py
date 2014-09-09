m = [
  ["#","#","#","#","#","#","#","0","#","#","#","#","#"],
  ["#"," "," "," "," "," ","#","0","#"," "," "," ","#"],
  ["#"," "," "," "," "," ","#","0","#"," "," "," ","#"],
  ["#"," "," "," "," "," ","#","0","#"," "," "," ","#"],
  ["#"," "," "," "," "," ","#","0","#","#","#","#","#"],
  ["#"," "," "," "," "," ","#","0"],
  ["#","#","#"," ","#","#","#","0"],
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
  {"type": "player", "position": (3,5), "sprite": "player.png"},
  {"type": "level", "position": (3,6), "level": "village1", "newposition": (16, 14)},
  {"type": "level", "position": (1,1), "newposition": (10,1), "sprite": "stairs.png"},
  {"type": "level", "position": (9,1), "newposition": (2,1), "sprite": "stairs.png"},
]
scripts = [
]
