#!/usr/bin/python3
def best_score(a_dictionary):
    m = min(a_dictionary.values())
    if m:
        return m
    else:
        return None
