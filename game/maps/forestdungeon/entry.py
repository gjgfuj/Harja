m = [
  ["#","#","#","#","#","#","#"],
  ["#"," "," "," "," "," ","#"],
  ["o","o","o","o","o","o","o"],
  ["#"," "," ","o"," "," ","#"],
  ["#"," "," ","o"," "," ","#"],
  ["#"," "," ","o"," "," ","#"],
  ["#","#","#","o","#","#","#"],
]
bindings = {
  "#": "brickwall.png",
  " ": "grass.png",
  "o": "brickfloor.png"
}
movement = {
  "#": False,
  " ": True,
  "o": True
}
events = [
  {"type": "player", "sprite": "player.png"},
]
scripts = [
  
]
