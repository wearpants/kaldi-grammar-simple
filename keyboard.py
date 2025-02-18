# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

try:
    from aenea import *
except:
    from dragonfly import *

try:
    from dragonfly.actions.keyboard import keyboard
    from dragonfly.actions.typeables import typeables
    if 'semicolon' not in typeables:
        typeables["semicolon"] = keyboard.get_typeable(char=';')
except:
    pass

from words import handle_word

release = Key("shift:up, ctrl:up, alt:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    try:
        from natlink import setMicState
        setMicState("sleeping")
        print("* Dictation canceled. Going to sleep. *")
    except:
        pass


# For repeating of characters.
specialCharMap = {
    "(bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|dit)": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk)": "*",
    "colon": ":",
    "(semicolon|semi colon)": ";",
    "at sign": "@",
    #"location": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",
    "space": " ",

    "bang": "!",
    "question [mark]": "?",
    "caret": "^",
    # some other symbols I haven't imported yet, lazy sorry
    # 'ampersand': Key('ampersand'),
    # 'apostrophe': Key('apostrophe'),
    # 'asterisk': Key('asterisk'),
    # 'at': Key('at'),
    # 'backslash': Key('backslash'),
    # 'backtick': Key('backtick'),
    # 'bar': Key('bar'),
    # 'caret': Key('caret'),
    # 'colon': Key('colon'),
    # 'comma': Key('comma'),
    # 'dollar': Key('dollar'),
    # #'(dot|period)': Key('dot'),
    # 'double quote': Key('dquote'),
    # 'equal': Key('equal'),
    # 'bang': Key('exclamation'),
    # 'hash': Key('hash'),
    # 'hyphen': Key('hyphen'),
    # 'minus': Key('minus'),
    # 'percent': Key('percent'),
    # 'plus': Key('plus'),
    # 'question': Key('question'),
    # # Getting Invalid key name: 'semicolon'
    # #'semicolon': Key('semicolon'),
    # 'slash': Key('slash'),
    # '[single] quote': Key('squote'),
    # 'tilde': Key('tilde'),
    # 'underscore | score': Key('underscore'),
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

letterMap = {
    "(alpha|arch)": "a",
    "(bravo|brav|beta) ": "b",
    "(charlie|turley) ": "c",
    "(delta) ": "d",
    "(echo) ": "e",
    "(foxtrot) ": "f",
    "(golf|gang|gobo) ": "g",
    "(hotel|hot) ": "h",
    "(india|igloo) ": "i",
    "(juliet|julia) ": "j",
    "(kilo) ": "k",
    "(lima|line|lion) ": "l",
    "(mike|mary) ": "m",
    "(novy|nancy) ": "n",
    "(Oscar) ": "o",
    "(papa|poppa) ": "p",
    "(queen|queer) ": "q",
    "(romeo|ralph) ": "r",
    "(sierra) ": "s",
    "(tango) ": "t",
    "(uniform) ": "u",
    "(victor) ": "v",
    "(whiskey) ": "w",
    "(x-ray) ": "x",
    "(yankee|yup|yep) ": "y",
    "(zulu|zipper) ": "z",
}
#letterMap = {
    #"(alpha|arch)": "a",
    #"(bravo|brav) ": "b",
    #"(charlie|turley|char) ": "c",
    #"(delta|del) ": "d",
    #"(echo|eck) ": "e",
    #"(foxtrot|fox) ": "f",
    #"(golf|gang) ": "g",
    #"(hotel) ": "h",
    #"(india|indigo|ish) ": "i",
    #"(juliet|julia) ": "j",
    #"(kilo) ": "k",
    #"(lima|lion|line|lie) ": "l",
    #"(mike) ": "m",
    #"(november|noy) ": "n",
    #"(Oscar|osh) ": "o",
    #"(papa|poppa|pom) ": "p",
    #"(quebec|quiche|queen) ": "q",
    #"(romeo|ree) ": "r",
    #"(sierra|soy) ": "s",
    #"(tango|tay) ": "t",
    #"(uniform|umm) ": "u",
    #"(victor|van) ": "v",
    #"(whiskey|wes) ": "w",
    #"(x-ray) ": "x",
    #"(yankee|yaa) ": "y",
    #"(zulu) ": "z",
#}


# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|caps) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|slap|lap)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)



grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Navigation keys.
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "page up [<n>]": Key("pgup:%(n)d"),
        "page down [<n>]": Key("pgdown:%(n)d"),
        #"up <n> (page|pages)": Key("pgup:%(n)d"),
        #"down <n> (page|pages)": Key("pgdown:%(n)d"),
        #"left <n> (word|words)": Key("c-left/3:%(n)d/10"),
        #"right <n> (word|words)": Key("c-right/3:%(n)d/10"),
        "home": Key("home"),
        "end": Key("end"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),
        # Functional keys.
        "(space|suss)": release + Key("space"),
        "(space|suss) [<n>]": release + Key("space:%(n)d"),
        "(enter|slap|lap) [<n>]": release + Key("enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
        "(delete|del) [<n>]": Key("del:%(n)d"),
        "(delete|del) line": Key("home, s-end, del"),  # @IgnorePep8
        "select line": Key("home, s-end"),  # @IgnorePep8
        "copy line": Key("home, s-end") + release + Key("c-c/3"),  # @IgnorePep8
        "cut line": Key("home, s-end") + release + Key("c-x/3"),  # @IgnorePep8                
        "(backspace|back|muss|mush) [<n>]": release + Key("backspace:%(n)d"),
        "application key": release + Key("apps/3"),
        "win key": release + Key("win/3"),
        "paste [that]": release + Key("c-v/3"),
        "copy [that]": release + Key("c-c/3"),
        "cut [that]": release + Key("c-x/3"),
        "select all": release + Key("c-a/3"),
        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,
        "press key <pressKey>": Key("%(pressKey)s"),
        # Closures.
        #"angle brackets": Key("langle, rangle, left/3"),
        #"[square] brackets": Key("lbracket, rbracket, left/3"),
        #"[curly] braces": Key("lbrace, rbrace, left/3"),
        #"(parens|parentheses)": Key("lparen, rparen, left/3"),
        #"quotes": Key("dquote/3, dquote/3, left/3"),
        #"backticks": Key("backtick:2, left"),
        #"single quotes": Key("squote, squote, left/3"),
        "(squiggle|tilda)": Text("~"),
        "backtick": Key("backtick"),
        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.
        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "(semicolon|semi colon) [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        #"(dot|period|dit|point)": Key("dot"),  # cannot be followed by a repeat count
        "(period|point)": Key("dot"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        #'(laip|len) [<n>]':   Key('lparen:%(n)d'),
        '(lip|lparen) [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        #'(raip|ren|wren) [<n>]':   Key('rparen:%(n)d'),
        '(rip|rparen) [<n>]':   Key('rparen:%(n)d'),

        "doc save": Key("c-s"),
        "doc open": Key("c-o"),
        "doc new": Key("c-n"),
        "doc quit": Key("c-q"),
        "undo": Key("c-z"),

        '(left wor|left word) [<n>]':  Key('c-left:%(n)d'),
        '(right wor|right word) [<n>]':  Key('c-right:%(n)d'),
        '(backwor|mushwor|mush word|muss word|mussword) [<n>]': Key('c-backspace:%(n)d'),
        '(delwor|del wor|delword|del word) [<n>]': Key('c-delete:%(n)d'),

        'suspend': Key('c-z'),

        'word <text>': Function(handle_word),
        'number <num>': Text("%(num)d"),
        #'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Microphone sleep/cancel started dictation.
        "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }

#class DigitRule(CompoundRule):
#    spec = "digits <digits>"
#    extras = [
#        Repetition(IntegerRef("digit", 1, 20), name="digits"),
#    ]
#
#    def _process_recognition(self, node, extras):
#        for action in extras["digits"]:
#            action.execute()