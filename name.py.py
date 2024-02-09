#!/usr/bin/env python3
"""
Exhaustive search. Works until a target string is found.
Checks all (26 + 1)**14 possible strings.
Should be run in a terminal for the best effect.

"""
import string
import itertools

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
	candidate = "".join(candidate)
	print(candidate, end="\r")
	if candidate == TARGET:
		break