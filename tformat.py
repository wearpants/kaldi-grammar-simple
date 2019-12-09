# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>

def format_underline(text):
    return '_'.join(text)


def format_camel(text):
    return  ''.join([word[0].upper() + word[1:] for word in text])


def format_proper(text):
    return ''.join(word.capitalize() for word in text)

   
def format_relpath(text):
    return '/'.join(text)


def format_abspath(text):
    return '/' + format_relpath(text)


def format_jumble(text):
    return ''.join(text)


def format_dotted(text):
    return '.'.join(text)


def format_dashes(text):
    return '-'.join(text)


def format_plain(text):
    return ' '.join(text)


def format_sentence(text):
    return ' '.join([text[0].capitalize()] + text[1:])


def format_title(text):
    return ' '.join((t.capitalize() for t in text))
