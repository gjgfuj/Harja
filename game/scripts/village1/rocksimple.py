script = [
  {"actions": [{"action": "test", "key": "pushcount", "test": "<", "value": 2, "index":2}, {"action": "add", "key": "pushcount", "value": 1}]},
  {"actions": [{"action": "changelevel", "level": "village1", "resetindex": True}]},
  {"speaker": "Archer", "line": "Yay!"},
  {"line": "You pushed the rock to the spot I wanted it."},
  {"line": "Good Job!"},
  {"actions": [{"action": "test", "key": "karma",  "test": ">", "value": 4, "index": 6}]},
  {"actions": [{"action": "add", "key": "karma",  "value": 5}]},
  {"actions": [{"action": "changelevel", "level": "village1"}]}
]
