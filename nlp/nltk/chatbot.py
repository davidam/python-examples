#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import nltk

# This instruction imports the nltk library into the current program.

def builtinEngines(whichOne):

# This instruction defines a new function called builtinEngines that takes a string parameter, whichOne:

    if whichOne == 'eliza': nltk.chat.eliza.demo()

    elif whichOne == 'iesha': nltk.chat.iesha.demo()

    elif whichOne == 'rude': nltk.chat.rude.demo()

    elif whichOne == 'suntsu': nltk.chat.suntsu.demo()

    elif whichOne == 'zen': nltk.chat.zen.demo()

    else:

        print("unknown built-in chat engine {}".format(whichOne))

chatpairs = (

(r"(.*?)Stock price(.*)", ("Today stock price is 100",

"I am unable to find out the stock price.")), (r"(.*?)not well(.*)",

("Oh, take care. May be you should visit a doctor", "Did you take some medicine ?")),

(r"(.*?)raining(.*)",

("Its monsoon season, what more do you expect ?", "Yes, its good for farmers")),

(r"How(.*?)health(.*)",

("I am always healthy.",

"I am a program, super healthy!")), (r".*",

("I am good. How are you today ?", "What brings you here ?"))

)


def chat():

    print("!"*80)

    print(" >> my Engine ")



for engine in ['eliza', 'iesha', 'rude', 'suntsu', 'zen']:

    print("=== demo of {} ===".format(engine) % builtinEngines(engine))

#        print() myEngine()
