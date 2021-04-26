# =================================================
# Riley Stewart - Tonkin (20684006)
# CS116 Winter 2017
# Assignment 09, Problem 2
# =================================================

# Purpose:
# function automation writes into a txt file with a length of
# each line of padding * 2 + 1 (excluding the new line character)
# and 'X' distributed throughout the list depending on the line

##===========================================================##

# Effects:
# the function automation writes into a file with the name
# given as the filename
# the list periods periods that is created has elements at
# position x to the string "X"
# the first or last character after the first mutation is mutated
# to the string "."

##===========================================================##

# Contract
# automation: str Nat Nat -> None

##===========================================================##

# Requires:
# filename must inclue suffix ".txt"
# padding > 0
# nlines > 0

##===========================================================##

# Examples:
# automation(E1, 3, 5) => None
# E1 == "a-3-5.txt"
# ...X...
# ..XXX..
# .X...X.
# .XX.XX.
# .......

##===========================================================##

# Primary Functon:
def automaton(filename, padding, nlines):
    i = 0
    f = open(filename, 'w')
    line = "." * padding + "X" + "." * padding + "\n"
    listing = list(line)
    line_writer = f.write(line)
    periods = ["."] * (2 * padding + 1) + ["\n"]

    while nlines - 1 > 0:
        while i < len(periods) - 1:
            if (listing[i-1]) == "X" and listing[i] == "."\
               and listing[i + 1] == ".":
                periods[i] = "X"
                i += 1
            elif (listing[i-1]) == "." and listing[i] == "X"\
                    and listing[i + 1] == ".":
                periods[i] = "X"
                i += 1
            elif (listing[i-1]) == "." and listing[i] == "."\
                    and listing[i + 1] == "X":
                periods[i] = "X"
                i += 1
            else:
                i += 1
        periods = "".join(periods)
        f.write(periods)
        listing = list(periods)
        i = 0
        periods = ["."] * (2 * padding + 1) + ["\n"]
        nlines -= 1
    f.close()
