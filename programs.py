# commands for controlling various programs

try:
    from aenea import *
except:
    from dragonfly import *

gitcommand_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in gitcommand_array:
    gitcommand[command] = command

class ProgramsRule(MappingRule):
    mapping = {
        "command (git|get)": Text("git "),
        "command (git|get) <gitcommand>": Text("git %(gitcommand)s "),
        "command nano": Text("nano "),
        "command C D": Text("cd "),
        "command list": Text("ls "),
        "command cat": Text("cat "),
        "command (grep|grip)": Text("grep -rn"),
        "command sudo": Text("sudo "),
        #"command background": Text("bg "),
        #"command foreground": Text("fg "),

        # web browser
        'address bar': Key('c-l'),
        'reload': Key('f5'),
        'really reload': Key('s-f5'),
        'go back [<n>]': Key('a-left:%(n)d'),
        'go forward [<n>]': Key('a-right:%(n)d'),
        'previous tab [<n>]': Key('c-pgup:%(n)d'),
        '(next|necks) tab [<n>]': Key('c-pgdown:%(n)d'),
        'new tab': Key('c-t'),
        'close tab': Key('c-w'),

        # Xfce-like desktop environment commands
        'really close window': Key('a-f4'),
        'switch window [<n>]': Key('a-tab:%(n)d'),
        'maximize window': Key('a-f10'),
        'minimize window': Key('a-f9'),

    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitcommand', gitcommand),
    ]
    defaults = {
        "n": 1,
    }
