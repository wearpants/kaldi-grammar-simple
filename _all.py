# _all.py: main rule for kaldi-grammar-simple grammar

from dragonfly import *

import keyboard
import words
import programs

release = Key("shift:up, ctrl:up, alt:up")

alternatives = []
alternatives.append(RuleRef(rule=keyboard.KeystrokeRule()))
#alternatives.append(RuleRef(rule=keyboard.DigitRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
alternatives.append(RuleRef(rule=words.ReFormatRule()))
alternatives.append(RuleRef(rule=words.NopeFormatRule()))
alternatives.append(RuleRef(rule=words.PhraseFormatRule()))
alternatives.append(RuleRef(rule=programs.ProgramsRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=16, name="sequence")

class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
            release.execute()

grammar = Grammar("root rule")
grammar.add_rule(RepeatRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

if __name__ == '__main__':
    #engine.list_available_microphones()
    execfile('kaldi_module_loader_plus.py')
