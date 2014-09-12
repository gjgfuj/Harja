m = [
  ["0","#","#","#","#","#","#","#"],
  ["#","#"," ","t","o"," ","t","#"],
  ["o","o","o","o","o"," "," ","#"],
  ["#","#","t"," ","o","t"," ","#"],
  ["0","#"," "," ","o"," ","t","#"],
  ["0","#"," ","t","o"," "," ","#"],
  ["0","#","#","#","o","#","#","#"]
]
bindings = {
  "#": "brickwall.png",
  " ": "grass.png",
  "o": "brickfloor.png",
  "t": "tree.png"
}
movement = {
  "#": False,
  " ": True,
  "o": True,
  "t": False
}
events = [
  {"type": "player", "sprite": "player.png"},
  {"type": "level", "position": (4,6), "level": "forest1", "newposition": (3, 15), "sprite": "stairs.png"},
  {"type": "level", "position": (0,2), "level": "forestdungeon.maze", "newposition": (7, 7)},
  {"type": "level", "position": (4,0), "level": "forestdungeon.central", "newposition": (6,17)}
]
scripts = [
  
]
mapname = "Forest Temple"
music = "Temple.ogg"
