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
   
from dragonfly.engines.backend_kaldi.dictation import CloudDictation

from keyboard import numberMap

class DictationRule(MappingRule):
  mapping = { "dictation <clouddict>": Text("%(clouddict)s") }
  extras = [ CloudDictation("clouddict") ]


class DigitsRule(CompoundRule):
    spec = "(digits|dijits) <digits>"
    extras = [
        Repetition(Choice("digit", numberMap), min=1, max=30, name="digits"),
    ]
    
    def _process_recognition(self, node, extras):
        words = node.words()
        print "digits rule:", words, extras
        return Text("".join(extras['digits'])).execute()