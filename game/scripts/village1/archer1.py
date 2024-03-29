script = [
  {"actions": [
    {"action": "setindex", "index": 10},
    {"action": "bgfile", "file": "archer.png"}
  ]},
  {"speaker": "Archer", "line": "How are you going, Harja."},
  {"actions": [
    {"action": "changelevel", "level": "village1", "resetindex": True},
    {"action": "set", "key": "spoken2"}
  ]},
  {"speaker": "Archer", "line": "I don't care.", "actions": [{"action": "add",  "key": "karma", "value": -1}]},
  {"actions": [
    {"action": "changelevel", "level": "village1", "resetindex": True}
  ]},
  {"speaker": "You", "line": "What's it to you."},
  {"speaker": "Archer", "line": "Well, that's very nice.", "actions": [{"action": "add",  "key": "karma", "value": -5}]},
  {"actions": [
    {"action": "changelevel", "level": "village1", "resetindex": True}
  ]},
  {"speaker": "Archer", "line": "I was going to ask you to do something, \nbut you have already done it."},
  {"actions": [{"action": "changelevel", "level": "village1", "resetindex": True}]},
  {"actions": [
    {"action": "test",  "key": "karma", "test": "<", "value": -10, "index": 5},
    {"action": "test", "key": "spoken2", "index": 3}
  ]},
  {"speaker": "Archer", "line": "Oh, good."},
  {"line": "You woke up."},
  {"actions": [
    {"action": "test", "key": "spoken", "index": 1}
  ]},
  {"line": "So, who are you?"},
  {"speaker": "You", "line": "I am..."},
  {"actions": [
    {"action": "menu", "options": ["Tell him your real name.", "Lie."]}
  ]},
  {"actions": [
    {"action": "test", "key": "menu", "value": "Lie.", "index": 5}
  ]},
  {"speaker": "Harja", "line": "Harja."},
  {"speaker": "Archer", "line": "Oh, that's cool. I'm Archer, the Archer."},
  {"actions": [
    {"action": "set", "key": "spoken"},
    {"action": "add", "key": "karma",  "value": 10}
  ]},
  {"actions": [{"action": "test", "key": "pushcount", "test": ">", "value": 1, "index": 7}]},
  {"line": "Hey, can I ask you to do something for me?"},
  {"line": "You see, I have two rocks around."},
  {"line": "Can you push them into the holes next to me?"},
  {"actions": [
    {"action": "changelevel", "level": "village1", "resetindex": True}
  ]},
]
