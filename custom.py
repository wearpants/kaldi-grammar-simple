# commands for controlling various programs

try:
    from aenea import *
except:
    from dragonfly import *

class CustomRule(MappingRule):
    mapping = {
        "memrise": Text("memrise"),
        "memflow": Text("memflow"),
        "braise": Text("braze"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
