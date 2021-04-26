# =================================================
# Riley Stewart - Tonkin (20684006)
# CS116 Winter 2017
# Assignment 09, Problem 3
# =================================================

# Purpose:
# function find_largest compares the elements in a graph, given
# as an adjacency list, which then compares which connected graph
# has the most connections

# function dfs take a graph, given as an adjacency list, and a
# string which is called within the graph. Then composes a list
# of all the connections to the set point

##===========================================================##

# Constants:
A = {"Dan": ["Carlos"],
     "Carlos": ["Dan"],
     "Bob": ["Ali", "Eve"],
     "Feng": ["Pat", "Ted", "Heidi"],
     "Ted": ["Feng"],
     "Heidi": ["Feng", "Sai"],
     "Ali": ["Bob", "Eve"],
     "Maria": [],
     "Eve": ["Bob", "Ali"],
     "Pat": ["Feng"],
     "Sai": ["Heidi"]}

##===========================================================##

# Contract
# find_largest: (dictof any) -> Nat
# dfs: (dictof any) any -> (listof any)

##===========================================================##

# Requires:
# len(graph) > 0
# dfs requires the parameter v to be within the parameter graph

##===========================================================##

# Examples:
# find_largest(A) => 5

##===========================================================##

# Helper Function:


def dfs(graph, v):
    visited = []
    S = [v]
    while S != []:
        v = S.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                if w not in visited:
                    S.append(w)
    return visited

##===========================================================##

# Primary Functon:


def find_largest(graph):
    lengths = []
    for i in graph:
        length_of_list = len(dfs(graph, i))
        lengths.append(length_of_list)
    return max(lengths)
