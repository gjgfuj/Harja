script = [
  {"actions": [{"action": "test", "key": "forestdungeon.unlocked", "index": 2}]},
  {"actions": [{"action": "setindex", "index": 3}]},
  {"actions": [{"action": "changelevel", "level": "hiddenvillage", "resetindex": True}]},
  {"line": "You see a hole where a stick can go through."},
  {"actions": [{"action": "test", "key": "forestleverstick", "index": 6}]},
  {"actions": [{"action": "setindex", "index": 2}]},
  {"line": "You stick the lever in the hole and pull it."},
  {"actions": [{"action": "set", "key": "forestdungeon.unlocked"}, {"action": "playsound", "sound": "Jingle1.ogg"}]},
  {"actions": [{"action": "changelevel", "level": "hiddenvillage", "resetindex": True}]}
]
