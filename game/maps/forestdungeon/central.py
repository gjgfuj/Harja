m = [
  ["0","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  [" ","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["#","#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
  ["0","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#"],
  ["0","0","0","0","0","t"," ","g"]
]
bindings = {
  "#": "brickwall.png",
  "g": "grass.png",
  " ": "brickfloor.png",
  "t": "tree.png"
}
movement = {
  "#": False,
  "g": True,
  " ": True,
  "t": False
}
events = [
  {"type": "player", "sprite": "player.png"},
  {"type": "level", "position": (0, 15), "level": "forestdungeon.maze", "newposition": (7, 2)},
  {"type": "level", "position": (6, 18), "level": "forestdungeon.centraltoentry"}
]
scripts = [
  "forestdungeon.centraltoentry"
]
mapname = "Forest Temple"
music = "Temple.ogg"
