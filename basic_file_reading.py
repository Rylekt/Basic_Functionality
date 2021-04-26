# =================================================
# Riley Stewart - Tonkin (20684006)
# CS116 Winter 2017
# Assignment 09, Problem 1
# =================================================

# Purpose:
# function find_winner takes in a txt file and evaluates an array
# of strings. It the calculates which of the teams predetermined
# in the string has the most points.

# function find_dict consumes a txt file and composes a dictionary
# of each of the teams within the text file
##===========================================================##
# Effects:
# find_winner opens up a file and reads to compose a dictionary
# of the scores of the teams stated in the file.
##===========================================================##
# Contract
# find_winner: Str -> Int
##===========================================================##

# Requires:
# filename must have the suffix ".txt"
# input file must have at least one line to evaluate
# lines in the file must have a team and a score parameter.

##===========================================================##

# Primary Functon:
def find_winner(filename):
    file = open(filename, "r")
    data = file.readline()
    teams = {}
    while data != "":
        comps = data.split(",")
        key = comps[0]
        if key in teams:
            teams[key] += int(comps[1])
            data = file.readline()
        else:
            teams[key] = int(comps[1])
            data = file.readline()
    file.close()
    scoring = list(teams.values())
    return max(scoring)
