#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  Copyright (C) 2026 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with python-examples; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

#  Solved exercises from https://course.spacy.io/en/chapter1

# 1.2 Getting Started: Languages
#     English, German and Spanish

# Import spaCy
import spacy

# Create the English nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)

# Create the German nlp object
nlp = spacy.blank("de")

# Process a text (this is German for: "Kind regards!")
doc = nlp("Liebe Grüße!")

# Print the document text
print(doc.text)

# Create the Spanish nlp object
nlp = spacy.blank("es")

# Process a text (this is Spanish for: "How are you?")
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)
